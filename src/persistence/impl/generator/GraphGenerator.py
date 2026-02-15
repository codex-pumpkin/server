from src.persistence.interfaces import IGraphGenerator
from PySpice.Spice.Parser import SpiceParser
import tempfile
import os
import json
import asyncio

class GraphGenerator(IGraphGenerator):
    async def gen_graph(self, code: str) -> str:
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".cir", delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_path = tmp_file.name

        try:
            parser = SpiceParser(path=tmp_path)
            circuit = parser.build_circuit()
            circute_dict = {}
            circuit_name = circuit.title if circuit.title.strip() else "main"
            circute_dict[circuit_name] = await self._parse_circuit(circuit.elements)

            for idx, subckt_stmt in enumerate(parser.subcircuits, start=1):
                subckt_name = subckt_stmt.name.strip() if subckt_stmt.name else f"{idx}:subckt"
                subckt_circute = subckt_stmt.build(ground=0)
                circute_dict[subckt_name] = await self._parse_circuit(subckt_circute.elements)

            return json.dumps(circute_dict, indent=2)
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

    async def _parse_circuit(self, circuit_elements):
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
* Complex Differential Amplifier Circuit
.SUBCKT DIFF_AMP 1 2 3 4
Q1 10 11 12 QNL
Q2 13 14 12 QNL
Q3 12 15 16 QNL
Q4 16 16 17 QNL
R1 1 10 1k
R2 2 13 1k
RC1 10 18 10k
RC2 13 18 10k
RBIAS 17 18 20k
C1 4 18 1u
VCC 18 0 DC 12
VEE 19 0 DC -12
VIN 1 0 AC 0.1 SIN(0 1k)
.MODEL QNL NPN BF=100 RB=50 CJE=5P CJC=3P TF=0.5N TR=10N
.ENDS
X1 1 2 3 4 DIFF_AMP
.TRAN 1N 100U
.PRINT TRAN V(4)
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
* Complex Differential Amplifier Circuit
.SUBCKT DIFF_AMP 1 2 3 4
Q1 10 11 12 QNL
Q2 13 14 12 QNL
Q3 12 15 16 QNL
Q4 16 16 17 QNL
R1 1 10 1k
R2 2 13 1k
RC1 11 18 10k
RC2 14 18 10k
RB1 15 18 20k
RB2 17 18 20k
C1 18 4 1u
C2 3 19 1u
VCC 18 20 DC 12
VEE 19 20 DC -12
VIN 1 0 AC 0.1 SIN(0 1k)
.MODEL QNL NPN BF=100 RB=50 CJE=5P CJC=3P TF=0.5N TR=10N
.ENDS
X1 1 2 3 4 DIFF_AMP
.TRAN 1N 100N UIC
.PRINT TRAN V(4) I(VIN)
.END


"""


if __name__ == "__main__":
    """Test function for simple circuits and MOSFET circuits"""
    async def main():
        test_circuit = test2
        generator = GraphGenerator()
        components = await generator.gen_graph(test_circuit)
        print(json.dumps(components, indent=2))

    asyncio.run(main())
