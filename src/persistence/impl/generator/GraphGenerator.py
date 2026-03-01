from src.persistence.interfaces import IGraphGenerator
from PySpice.Spice.Parser import SpiceParser
import tempfile
import os
import json
import asyncio

class GraphGenerator(IGraphGenerator):
    async def gen_graph(self, code: str) -> str:
        """Generate a flattened graph representation of the circuit."""
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".cir", delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_path = tmp_file.name

        try:
            parser = SpiceParser(path=tmp_path)

            # Build main circuit
            main_circuit = parser.build_circuit()

            # Collect all subcircuit definitions
            subcircuit_defs = {sub.name: sub for sub in parser.subcircuits}

            # Flatten the main circuit into a list of primitive components (dicts)
            flat_components = self._flatten_elements(
                main_circuit.elements,
                subcircuit_defs,
                instance_prefix='',
                node_mapping={}
            )

            # Optional: remove floating nodes (components with no connections)
            flat_components = self._remove_floating_from_flat(flat_components)

            # Build graph data (nodes + edges)
            graph_data = self._build_graph_data(flat_components)

            return json.dumps(graph_data, indent=2)

        except Exception as e:
            print(f"ERROR parsing circuit: {e}")
            import traceback
            traceback.print_exc()
            raise
        finally:
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    def _flatten_elements(self, elements, subcircuit_defs, instance_prefix='', node_mapping=None):
        """
        Recursively flatten a list of circuit elements.
        - elements: list from Circuit.elements
        - subcircuit_defs: dict {name: SubCircuit}
        - instance_prefix: string to prepend to internal nodes (e.g., 'X1_')
        - node_mapping: dict {formal_pin: actual_node} for the current context
        Returns a list of primitive component dictionaries (as from _extract_component_data).
        """
        if node_mapping is None:
            node_mapping = {}
        flat = []

        for element in elements:
            elem_class = element.__class__.__name__

            # Skip subcircuit definitions themselves (they appear only in parser.subcircuits)
            if 'SubCircuitDefinition' in elem_class:
                continue

            # Extract component data using existing method (returns dict)
            comp_data = self._extract_component_data_sync(element)   # we'll create a sync version
            if not comp_data.get('nodes'):
                # Might be a model or other non‑connection object; keep as is?
                flat.append(comp_data)
                continue

            # Check if this is a subcircuit instance
            is_instance = False
            sub_name = None

            # PySpice subcircuit instances typically have class name 'SubCircuitElement' or similar
            if 'SubCircuit' in elem_class and 'Definition' not in elem_class:
                is_instance = True
                # Try to get subcircuit name from element attributes
                if hasattr(element, 'subcircuit_name'):
                    sub_name = element.subcircuit_name
                elif hasattr(element, 'model_name'):
                    sub_name = element.model_name
                # Check if element has a subcircuit attribute (be careful with PySpice's __getattr__)
                else:
                    try:
                        if hasattr(element, '__dict__') and 'subcircuit_name' in element.__dict__:
                            sub_name = element.__dict__['subcircuit_name']
                    except:
                        pass

            if is_instance:
                # If we couldn't find the name, try to match by examining available definitions
                if not sub_name and len(subcircuit_defs) > 0:
                    # Maybe the element name gives us a clue (instances usually start with X)
                    # For now, skip if we can't determine
                    print(f"Warning: Could not determine subcircuit type for instance {element.name}")
                    # Treat as primitive component instead
                    is_instance = False

                if is_instance and sub_name:
                    definition = subcircuit_defs.get(sub_name)
                    if definition is None:
                        # Unknown subcircuit – treat as primitive
                        print(f"Warning: Unknown subcircuit {sub_name} in instance {element.name}")
                        is_instance = False
                    else:
                        # Build the definition's internal circuit
                        def_circuit = definition.build(ground=0)

                        # Try different attribute names for pins/parameters
                        formal_pins = []
                        if hasattr(definition, 'parameters'):
                            formal_pins = [str(p) for p in definition.parameters]
                        elif hasattr(definition, 'nodes'):
                            formal_pins = [str(p) for p in definition.nodes]
                        elif hasattr(definition, 'pins'):
                            formal_pins = [str(p) for p in definition.pins]
                        elif hasattr(definition, 'external_nodes'):
                            formal_pins = [str(p) for p in definition.external_nodes]

                        if not formal_pins:
                            print(f"Warning: Could not extract pins from subcircuit {sub_name}")
                            is_instance = False
                            continue
                        # Actual nodes from the instance (in same order)
                        actual_nodes = [str(n) for n in element.nodes]

                        # Create mapping for this instance
                        inst_mapping = dict(zip(formal_pins, actual_nodes))

                        # New prefix for internal nodes (instance name + '_')
                        new_prefix = f"{instance_prefix}{element.name}_"

                        # Recursively flatten the definition's elements
                        sub_flat = self._flatten_elements(
                            def_circuit.elements,
                            subcircuit_defs,
                            instance_prefix=new_prefix,
                            node_mapping=inst_mapping
                        )
                        flat.extend(sub_flat)

            if not is_instance:
                # Primitive component – apply node mapping and prefix to nodes
                new_nodes = []
                for node in comp_data.get('nodes', []):
                    node_str = str(node)
                    # If node is in mapping, replace with actual node
                    if node_str in node_mapping:
                        new_nodes.append(node_mapping[node_str])
                    else:
                        # If node is not ground, prefix it
                        if node_str != '0' and instance_prefix:
                            new_nodes.append(f"{instance_prefix}{node_str}")
                        else:
                            new_nodes.append(node_str)
                comp_data['nodes'] = new_nodes
                flat.append(comp_data)

        return flat

    # Synchronous wrapper for _extract_component_data (since flattening is not async)
    def _extract_component_data_sync(self, element):
        """Synchronous version of _extract_component_data (avoids awaiting)."""
        # Reuse the same logic, but without async/await.
        nodes = []
        element_class = element.__class__.__name__

        if 'SubCircuit' in element_class:
            if hasattr(element, 'parameters'):
                nodes = [str(param) for param in element.parameters]
            elif hasattr(element, 'interface'):
                nodes = [str(pin) for pin in element.interface]

        if not nodes:
            if hasattr(element, 'nodes'):
                try:
                    nodes_attr = element.nodes
                    if nodes_attr:
                        nodes = [str(node) for node in nodes_attr]
                except:
                    pass
            if not nodes and hasattr(element, 'pins'):
                try:
                    pins_attr = element.pins
                    if pins_attr:
                        nodes = [str(pin) for pin in pins_attr]
                except:
                    pass
            if not nodes:
                pin_attrs = []
                for i in range(1, 10):
                    attr_name = f'pin{i}'
                    if hasattr(element, attr_name):
                        try:
                            pin_val = getattr(element, attr_name)
                            if pin_val is not None:
                                pin_attrs.append(str(pin_val))
                        except:
                            pass
                if pin_attrs:
                    nodes = pin_attrs
            if not nodes:
                if hasattr(element, 'positive_node') and hasattr(element, 'negative_node'):
                    try:
                        pos = element.positive_node
                        neg = element.negative_node
                        if pos is not None:
                            nodes.append(str(pos))
                        if neg is not None:
                            nodes.append(str(neg))
                    except:
                        pass

        data = {
            "name": element.name,
            "type": element_class,
            "nodes": nodes,
        }

        # Extract values synchronously (reuse same logic without async)
        values = self._extract_all_values_sync(element)
        if values:
            data["values"] = values

        return data

    def _extract_all_values_sync(self, element):
        """Synchronous version of _extract_all_values."""
        values = {}
        comp_type = element.__class__.__name__

        primary_attrs = {
            'Resistor': 'resistance',
            'Capacitor': 'capacitance',
            'BehavioralCapacitor': 'capacitance_expression',
            'Inductor': 'inductance',
            'VoltageSource': 'dc_value',
            'CurrentSource': 'dc_value',
            'VCCS': 'gain',
            'VCVS': 'gain',
            'Mosfet': 'width',
        }
        primary_attr = primary_attrs.get(comp_type)
        if primary_attr and hasattr(element, primary_attr):
            val = getattr(element, primary_attr)
            if val is not None:
                values[primary_attr] = val.string_value if hasattr(val, 'string_value') else str(val)

        component_attrs = {
            'Mosfet': ['length', 'drain_area', 'source_area', 'drain_perimeter',
                       'source_perimeter', 'drain_number_square', 'source_number_square',
                       'multiplier', 'nfin', 'temperature', 'ic'],
            'Diode': ['area', 'pj', 'multiplier', 'temperature', 'ic'],
            'BJT': ['area', 'areac', 'areab', 'm', 'sens_area', 'multiplier', 'temperature', 'ic'],
            'Resistor': ['multiplier', 'scale', 'temperature', 'ac', 'noisy'],
        }
        if comp_type in component_attrs:
            for attr in component_attrs[comp_type]:
                if hasattr(element, attr) and (val := getattr(element, attr)) is not None:
                    values[attr] = val.string_value if hasattr(val, 'string_value') else str(val)

        if hasattr(element, 'waveform'):
            waveform = element.waveform
            values['waveform_type'] = waveform.__class__.__name__
            waveform_attrs = ['amplitude', 'frequency', 'delay', 'duty_cycle', 'rise_time',
                              'fall_time', 'pulse_width', 'phase', 'offset', 'ac', 'dc']
            for attr in waveform_attrs:
                if hasattr(waveform, attr) and (val := getattr(waveform, attr)) is not None:
                    values[f'waveform_{attr}'] = val.string_value if hasattr(val, 'string_value') else str(val)

        return values

    # ----------------------------------------------------------------------
    # Graph building
    # ----------------------------------------------------------------------
    def _build_graph_data(self, flat_components):
        """
        Convert flat list of component dicts into a simple list format.
        Each component has: name, type, nodes (list), and values.
        """
        components_list = []
        all_nodes = set()

        for comp in flat_components:
            comp_name = comp.get('name', 'unknown')
            comp_type = comp.get('type', '')
            comp_nodes = comp.get('nodes', [])
            values = comp.get('values', {})

            # Collect all nodes
            all_nodes.update(comp_nodes)

            # Add component with its node list
            component_entry = {
                'name': comp_name,
                'type': comp_type,
                'nodes': comp_nodes,
                'values': values
            }
            components_list.append(component_entry)

        return {'components': components_list}

    def _remove_floating_from_flat(self, flat_components):
        """
        Remove components that only connect to nodes appearing in exactly one component.
        (Similar to _find_floating_nodes but on flat list.)
        """
        from collections import defaultdict
        node_to_comps = defaultdict(set)
        for idx, comp in enumerate(flat_components):
            for node in comp.get('nodes', []):
                node_to_comps[node].add(idx)   # store index, not name

        floating_nodes = {node for node, comps in node_to_comps.items()
                          if node != '0' and len(comps) <= 1}

        # Keep components that have at least one non‑floating node
        filtered = []
        for comp in flat_components:
            comp_nodes = set(comp.get('nodes', []))
            if comp_nodes - floating_nodes:
                filtered.append(comp)
        return filtered


    def _find_floating_nodes(self, components: list) -> set:
        """
        A node is floating if:
          - It only appears in a single component, OR
          - All its appearances are within the same component (e.g. R_ghost 5 5)
        Ground node (0) is always excluded.
        """
        from collections import defaultdict

        node_to_components = defaultdict(set)  # node -> set of component names that use it

        for component in components:
            comp_name = component.get("name", "unknown")
            nodes = component.get("nodes", [])
            unique_nodes_in_comp = set(nodes)  # deduplicate within same component
            for node in unique_nodes_in_comp:
                node_to_components[node].add(comp_name)

        floating = set()
        for node, comps in node_to_components.items():
            if node == "0":  # ground is never floating
                continue
            if len(comps) <= 1:  # only seen by one (or zero) components
                floating.add(node)

        return floating

    async def _parse_circuit(self, circuit_elements):
        """Parse circuit."""
        components = []
        for element in circuit_elements:
            try:
                # Skip only subcircuit definitions, not instances
                element_class = element.__class__.__name__
                if 'SubCircuitDefinition' in element_class:
                    print(f"DEBUG: Skipping SubCircuit definition: {element.name}")
                    continue

                component_data = await self._extract_component_data(element)

                # Only add if we got nodes or it's a specific type we want
                if component_data.get("nodes") or element_class in ['Model']:
                    components.append(component_data)
                else:
                    print(f"Skipped (no nodes): {component_data}")

            except Exception as e:
                print(f"Error extracting element {element}: {e}")
                import traceback
                traceback.print_exc()
                # Continue with other elements even if one fails
                continue
        return components

    async def _extract_component_data(self,element):
        """Extract component data as a dictionary"""
        # Extract nodes with fallback logic for different PySpice element types
        nodes = []
        element_class = element.__class__.__name__


        # Handle SubCircuit definitions - they have parameters instead of nodes
        if 'SubCircuit' in element_class:
            # SubCircuits have parameters which are the interface pins
            if hasattr(element, 'parameters'):
                nodes = [str(param) for param in element.parameters]
            elif hasattr(element, 'interface'):
                nodes = [str(pin) for pin in element.interface]

        # Try different node attributes based on element type
        if not nodes:
            # Try nodes attribute first
            if hasattr(element, 'nodes'):
                try:
                    nodes_attr = element.nodes
                    if nodes_attr:
                        nodes = [str(node) for node in nodes_attr]
                except Exception as e:
                    print(f"DEBUG: Error extracting nodes attribute: {e}")

            # Try pins attribute
            if not nodes and hasattr(element, 'pins'):
                try:
                    pins_attr = element.pins
                    if pins_attr:
                        nodes = [str(pin) for pin in pins_attr]
                except Exception as e:
                    print(f"DEBUG: Error extracting pins: {e}")

            # Try individual pin attributes
            if not nodes:
                pin_attrs = []
                for i in range(1, 10):
                    attr_name = f'pin{i}'
                    if hasattr(element, attr_name):
                        try:
                            pin_val = getattr(element, attr_name)
                            if pin_val is not None:
                                pin_attrs.append(str(pin_val))
                        except:
                            pass
                if pin_attrs:
                    nodes = pin_attrs

            # Try positive/negative node for sources
            if not nodes:
                if hasattr(element, 'positive_node') and hasattr(element, 'negative_node'):
                    try:
                        pos = element.positive_node
                        neg = element.negative_node
                        if pos is not None:
                            nodes.append(str(pos))
                        if neg is not None:
                            nodes.append(str(neg))
                    except Exception as e:
                        print(f"DEBUG: Error extracting positive/negative nodes: {e}")

        # Debug: print all attributes if nodes are still empty
        if not nodes:
            all_attrs = [attr for attr in dir(element) if not attr.startswith('_')]
            # Try to print first few non-private attributes
            for attr in all_attrs[:10]:
                try:
                    val = getattr(element, attr)
                    print(f"  {attr}: {val} (type: {type(val).__name__})")
                except:
                    pass

        data = {
            "name": element.name,
            "type": element_class,
            "nodes": nodes,
        }

        values = await self._extract_all_values(element)
        if values:
            data["values"] = values

        return data

    async def _extract_all_values(self, element):
        """Extract primary value and parameters, merged without duplicates"""
        values = {}
        comp_type = element.__class__.__name__

        primary_attrs = {
            'Resistor': 'resistance',
            'Capacitor': 'capacitance',
            'BehavioralCapacitor': 'capacitance_expression',
            'Inductor': 'inductance',
            'VoltageSource': 'dc_value',
            'CurrentSource': 'dc_value',
            'VCCS': 'gain',
            'VCVS': 'gain',
            'Mosfet': 'width',
        }

        primary_attr = primary_attrs.get(comp_type)
        if primary_attr and hasattr(element, primary_attr):
            val = getattr(element, primary_attr)
            if val is not None:
                values[primary_attr] = val.string_value if hasattr(val, 'string_value') else str(val)

        component_attrs = {
            'Mosfet': ['length', 'drain_area', 'source_area', 'drain_perimeter',
                       'source_perimeter', 'drain_number_square', 'source_number_square',
                       'multiplier', 'nfin', 'temperature', 'ic'],
            'Diode': ['area', 'pj', 'multiplier', 'temperature', 'ic'],
            'BJT': ['area', 'areac', 'areab', 'm', 'sens_area', 'multiplier', 'temperature', 'ic'],
            'Resistor': ['multiplier', 'scale', 'temperature', 'ac', 'noisy'],
        }

        if comp_type in component_attrs:
            for attr in component_attrs[comp_type]:
                if hasattr(element, attr) and (val := getattr(element, attr)) is not None:
                    values[attr] = val.string_value if hasattr(val, 'string_value') else str(val)

        if hasattr(element, 'waveform'):
            waveform = element.waveform
            values['waveform_type'] = waveform.__class__.__name__
            waveform_attrs = ['amplitude', 'frequency', 'delay', 'duty_cycle', 'rise_time',
                              'fall_time', 'pulse_width', 'phase', 'offset', 'ac', 'dc']
            for attr in waveform_attrs:
                if hasattr(waveform, attr) and (val := getattr(waveform, attr)) is not None:
                    values[f'waveform_{attr}'] = val.string_value if hasattr(val, 'string_value') else str(val)

        return values



test1 = """
* Common Emitter Amplifier Test
Vcc 1 0 DC 12V
Vin 2 0 AC 1 SIN(0 0.01 1k) ; AC source with transient
R1 1 3 22k
R2 3 0 4.7k
RC 1 4 2.2k
RE 5 0 1k
C1 2 3 10uF
C2 4 6 10uF
C3 5 0 100uF
RL 6 0 10k
Q1 4 3 5 Q2N2222

* Analysis
.OP
.AC DEC 20 10 100MEG
.TRAN 0.01ms 5ms
.MODEL Q2N2222 NPN(IS=14.34f BF=255.9 NF=1 VAF=74.03)
.END

"""

test2 = """
* SIMPLE DIFFERENTIAL AMPLIFIER WITH RESISTOR MODEL
.SUBCKT SIMPLE_DIFF_AMP 1 2 3 4 5 6 7 8 9
Ql 100 102 106 QNL
Q2 101 103 106 QNL
Q3 106 107 109 QNL
Q4 107 107 109 QNL
RS1 1 2 1000
RS2 3 2 1000
RC1 100 108 10000
RC2 101 108 10000
RBIAS 107 108 20000
VCC 8 0 DC 12
VEE 9 0 DC -12
VIN 1 0 AC 0.1 SIN(0 1)
.MODEL QNL NPN BF=80 RB=100 CCS=2P TF=0.3N CJE=3P CJC=2P VAF=SO
.ENDS SIMPLE_DIFF_AMP
* Analysis command
.TRAN 5N 10U
* Output requests
.PRINT TRAN V(5)
.END
"""

test3 = """
* Circuit with 2 MOSFETs and 2 resistors, 7 hour transient simulation
.model MOSN NMOS (VTO=1 KP=50u)
V1 1 0 DC 5
R3 1 2 1000
R1 2 0 1000
M1 3 1 0 0 MOSN W=1u L=0.18u
M2 0 2 0 0 MOSN W=1u L=0.18u
Vgate1 3 0 DC 5
Vgate2 4 0 DC 5
Rgate2 4 2 1meg
.TRAN 0.0001 25200
.PRINT TRAN V(1) V(2) V(3) V(4) I(V1)
.END
"""


test4 =  """
* Complex Differential Amplifier Circuit
.SUBCKT DIFF_AMP 1 2 3 4
Q1 10 11 12 QNL
Q2 13 14 12 QNL
Q3 12 15 16 QNL
Q4 16 17 18 QNL
R1 1 10 1k
R2 2 13 1k
RC1 11 19 10k
RC2 14 19 10k
RB1 17 19 20k
VCC 19 0 DC 12
VEE 18 0 DC -12
.model QNL NPN BF=100 RB=50 CJE=5p CJC=3p TF=0.2n TR=5n
.ENDS DIFF_AMP

* Main Circuit
V1 1 0 SIN(0 0.1 1k)
X1 1 2 3 4 DIFF_AMP
RLOAD 4 0 1k
.TRAN 1m 10m
.PRINT TRAN V(4)
.END
"""

test5 = """
* Four-Bit Binary Adder Using Bipolar NAND Gates
.MODEL QMOD NPN BF=20 RB=100 TF=0.1NS CJC=2PF
.MODEL DMOD D(IS=1E-14)

.SUBCKT NAND 1 2 3 4
* Nodes: 1=input1, 2=input2, 3=output, 4=VCC
Q1 9 5 1 QMOD
D1CLAMP 0 1 DMOD
Q2 9 5 2 QMOD
D2CLAMP 0 2 DMOD
RB 4 5 4K
R1 4 6 1.6K
Q3 6 9 8 QMOD
R2 8 0 1K
RC 4 7 130
Q4 7 6 10 QMOD
DVBEDROP 10 3 DMOD
Q5 3 8 0 QMOD
.ENDS NAND

.SUBCKT ONEBIT 1 2 3 4 5 6
* Nodes: 1=input A, 2=input B, 3=carry-in, 4=output sum, 5=carry-out, 6=VCC
X1 1 2 7 6 NAND
X2 1 7 8 6 NAND
X3 2 7 9 6 NAND
X4 8 9 10 6 NAND
X5 3 10 11 6 NAND
X6 3 11 12 6 NAND
X7 10 11 13 6 NAND
X8 12 13 4 6 NAND
X9 11 7 5 6 NAND
.ENDS ONEBIT

.SUBCKT FOURBIT 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
* Nodes: inputs A0-A3(1,3,5,7), inputs B0-B3(2,4,6,8),
* carry-in(9), outputs S0-S3(10,11,12,13), carry-out(14), VCC(15)
XBIT0 1 2 9 10 16 15 ONEBIT
XBIT1 3 4 16 11 17 15 ONEBIT
XBIT2 5 6 17 12 18 15 ONEBIT
XBIT3 7 8 18 13 14 15 ONEBIT
.ENDS FOURBIT

* Power supply
VCC 15 0 DC 5

* Input pulse sources for bits A and B and carry-in
VA0 1 0 PULSE(0 5 0 10NS 10NS 100NS 200NS)
VB0 2 0 PULSE(0 5 50NS 10NS 10NS 100NS 200NS)
VA1 3 0 PULSE(0 5 0 10NS 10NS 200NS 400NS)
VB1 4 0 PULSE(0 5 50NS 10NS 200NS 400NS 400NS)
VA2 5 0 PULSE(0 5 0 10NS 10NS 400NS 800NS)
VB2 6 0 PULSE(0 5 50NS 10NS 400NS 800NS 800NS)
VA3 7 0 PULSE(0 5 0 10NS 10NS 800NS 1600NS)
VB3 8 0 PULSE(0 5 50NS 10NS 800NS 1600NS 1600NS)
VCIN 9 0 PULSE(0 5 0 10NS 10NS 1600NS 3200NS)

* Instantiate four-bit adder
XADD 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 FOURBIT

* Load resistors on outputs for stable DC paths
RLOAD0 10 0 1K
RLOAD1 11 0 1K
RLOAD2 12 0 1K
RLOAD3 13 0 1K
RLOADCOUT 14 0 1K

.TRAN 1NS 3200NS UIC
.PRINT TRAN V(10) V(11) V(12) V(13) V(14)
.END
"""

test6 = """
* RC Circuit with a Floating Node
* ------------------------------------

V1 1 0 DC 5V
R1 1 2 1k
C1 2 0 10u
R2 2 3 2.2k
C2 3 0 4.7u

* --- Floating node below ---
* Node 5 is connected to nothing. It just exists. It floats.
R_ghost 5 5 1MEG

.tran 1ms 100ms
.probe V(1) V(2) V(3)
.end
"""
if __name__ == "__main__":
    """Test function for simple circuits and MOSFET circuits"""
    async def main():
        """Main."""
        test_circuit = test5
        generator = GraphGenerator()
        components = await generator.gen_graph(test_circuit)
        print(components)

    asyncio.run(main())
