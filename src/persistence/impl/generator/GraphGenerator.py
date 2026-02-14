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
            circuit = SpiceParser(path=tmp_path).build_circuit()
            components = []
            for element in circuit.elements:
                component_data = await self.extract_component_data(element)
                components.append(component_data)
            return components
        finally:
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    async def extract_component_data(self,element):
        """Extract component data as a dictionary"""
        data = {
            "name": element.name,
            "type": element.__class__.__name__,
            "nodes": [str(node) for node in element.nodes],
        }

        values = await self.extract_all_values(element)
        if values:
            data["values"] = values

        return data

    async def extract_all_values(self, element):
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


if __name__ == "__main__":
    """Test function for simple circuits and MOSFET circuits"""
    async def main():
        test_circuit = """
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
        generator = GraphGenerator()
        components = await generator.gen_graph(test_circuit)
        print(json.dumps(components, indent=2))

    asyncio.run(main())
