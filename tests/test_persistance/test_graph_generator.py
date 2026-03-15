import asyncio
import importlib
import json
import types

import pytest


graph_module = importlib.import_module("src.persistence.impl.generator.GraphGenerator")
GraphGenerator = graph_module.GraphGenerator


def _make_element(class_name, name="E1", **attrs):
    cls = type(class_name, (), {})
    obj = cls()
    obj.name = name
    for key, value in attrs.items():
        setattr(obj, key, value)
    return obj


def test_build_graph_and_floating_helpers():
    generator = GraphGenerator()
    flat = [
        {"name": "R1", "type": "Resistor", "nodes": ["1", "0"], "values": {"resistance": "1k"}},
        {"name": "R2", "type": "Resistor", "nodes": ["2", "2"], "values": {}},
    ]

    graph = generator._build_graph_data(flat)
    filtered = generator._remove_floating_from_flat(flat)
    floating = generator._find_floating_nodes(flat)

    assert graph["components"][0]["name"] == "R1"
    assert len(filtered) == 1
    assert floating == {"1", "2"}


def test_extract_component_data_sync_variants():
    generator = GraphGenerator()
    waveform = types.SimpleNamespace(
        __class__=types.SimpleNamespace(__name__="SineWave"),
        amplitude=types.SimpleNamespace(string_value="5"),
        frequency=types.SimpleNamespace(string_value="1k"),
    )

    resistor = _make_element(
        "Resistor",
        name="R1",
        nodes=["1", "0"],
        resistance=types.SimpleNamespace(string_value="1k"),
        multiplier=2,
        waveform=waveform,
    )
    pin_based = _make_element("CustomPart", name="X1", pin1="3", pin2="4")
    pn_source = _make_element("VoltageSource", name="V1", positive_node="5", negative_node="0", dc_value=10)
    subckt = _make_element("SubCircuitElement", name="XAMP", parameters=["IN", "OUT"])

    resistor_data = generator._extract_component_data_sync(resistor)
    pin_data = generator._extract_component_data_sync(pin_based)
    source_data = generator._extract_component_data_sync(pn_source)
    subckt_data = generator._extract_component_data_sync(subckt)

    assert resistor_data["nodes"] == ["1", "0"]
    assert resistor_data["values"]["resistance"] == "1k"
    assert resistor_data["values"]["multiplier"] == "2"
    assert resistor_data["values"]["waveform_amplitude"] == "5"
    assert pin_data["nodes"] == ["3", "4"]
    assert source_data["nodes"] == ["5", "0"]
    assert source_data["values"]["dc_value"] == "10"
    assert subckt_data["nodes"] == ["IN", "OUT"]


@pytest.mark.asyncio
async def test_extract_component_data_async_and_parse_circuit():
    generator = GraphGenerator()
    good = _make_element("Resistor", name="R1", nodes=["1", "0"], resistance=1)
    model = _make_element("Model", name="M1")
    bad = _make_element("BrokenPart", name="B1")

    async def fake_extract(element):
        if element.name == "B1":
            raise RuntimeError("boom")
        return {"name": element.name, "nodes": getattr(element, "nodes", [])}

    generator._extract_component_data = fake_extract
    parsed = await generator._parse_circuit(
        [
            _make_element("SubCircuitDefinitionThing", name="DEF"),
            good,
            model,
            bad,
        ]
    )

    assert parsed == [{"name": "R1", "nodes": ["1", "0"]}, {"name": "M1", "nodes": []}]


def test_flatten_elements_handles_primitives_and_subcircuits():
    generator = GraphGenerator()
    primitive = _make_element("Resistor", name="RMAIN", nodes=["1", "0"])
    unknown_instance = _make_element("SubCircuitThing", name="XUNK", nodes=["1", "2"], subcircuit_name="MISSING")
    known_instance = _make_element("SubCircuitThing", name="X1", nodes=["10", "20"], subcircuit_name="AMP")
    no_name_instance = _make_element("SubCircuitThing", name="X2", nodes=["10", "20"])
    internal = _make_element("Resistor", name="RINT", nodes=["IN", "N1"])

    definition = types.SimpleNamespace(
        parameters=["IN", "OUT"],
        build=lambda ground=0: types.SimpleNamespace(elements=[internal]),
    )

    flattened = generator._flatten_elements(
        [primitive, unknown_instance, known_instance, no_name_instance],
        {"AMP": definition},
    )

    assert any(comp["name"] == "RMAIN" for comp in flattened)
    assert any(comp["name"] == "XUNK" for comp in flattened)
    assert any(comp["name"] == "X2" for comp in flattened)
    assert any(comp["nodes"] == ["10", "X1_N1"] for comp in flattened)


def test_flatten_elements_handles_missing_pins_and_prefixed_nodes():
    generator = GraphGenerator()
    known_instance = _make_element("SubCircuitThing", name="X3", nodes=["7", "8"], subcircuit_name="NOPINS")
    internal = _make_element("Resistor", name="RINT", nodes=["A", "B"])

    definition = types.SimpleNamespace(
        build=lambda ground=0: types.SimpleNamespace(elements=[internal]),
    )

    flattened = generator._flatten_elements(
        [known_instance],
        {"NOPINS": definition},
        instance_prefix="TOP_",
        node_mapping={"A": "1"},
    )

    assert flattened == []


@pytest.mark.asyncio
async def test_async_extract_component_data_and_values_paths():
    generator = GraphGenerator()
    waveform = types.SimpleNamespace(
        __class__=types.SimpleNamespace(__name__="PulseWave"),
        delay=types.SimpleNamespace(string_value="1n"),
        duty_cycle=50,
    )
    resistor = _make_element(
        "Resistor",
        name="R1",
        nodes=["1", "0"],
        resistance=types.SimpleNamespace(string_value="2k"),
        multiplier=2,
        waveform=waveform,
    )
    source = _make_element("VoltageSource", name="V1", positive_node="3", negative_node="0", dc_value=5)
    pin_part = _make_element("CustomPart", name="X4", pin1="3", pin2="4")
    subckt = _make_element("SubCircuitThing", name="X5", interface=["IN", "OUT"])
    mosfet = _make_element("Mosfet", name="M1", width="1u", length="2u", multiplier=3)

    resistor_data = await generator._extract_component_data(resistor)
    source_data = await generator._extract_component_data(source)
    pin_data = await generator._extract_component_data(pin_part)
    subckt_data = await generator._extract_component_data(subckt)
    mosfet_values = await generator._extract_all_values(mosfet)

    assert resistor_data["values"]["resistance"] == "2k"
    assert resistor_data["values"]["waveform_delay"] == "1n"
    assert source_data["nodes"] == ["3", "0"]
    assert pin_data["nodes"] == ["3", "4"]
    assert subckt_data["nodes"] == ["IN", "OUT"]
    assert mosfet_values["width"] == "1u"
    assert mosfet_values["length"] == "2u"


@pytest.mark.asyncio
async def test_parse_circuit_skips_empty_component(monkeypatch):
    generator = GraphGenerator()
    printed = []

    async def fake_extract(element):
        return {"name": element.name, "nodes": []}

    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(args))
    generator._extract_component_data = fake_extract

    parsed = await generator._parse_circuit([_make_element("Resistor", name="R0")])

    assert parsed == []
    assert any("Skipped" in str(args[0]) for args in printed)


@pytest.mark.asyncio
async def test_gen_graph_uses_parser_and_cleans_tempfile(monkeypatch):
    removed = []

    class FakeTmp:
        name = "temp.cir"

        def write(self, code):
            self.code = code

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    class FakeParser:
        def __init__(self, path):
            self.path = path
            self.subcircuits = []

        def build_circuit(self):
            return types.SimpleNamespace(elements=["element"])

    monkeypatch.setattr(graph_module.tempfile, "NamedTemporaryFile", lambda **kwargs: FakeTmp())
    monkeypatch.setattr(graph_module, "SpiceParser", FakeParser)
    monkeypatch.setattr(graph_module.os, "remove", lambda path: removed.append(path))

    generator = GraphGenerator()
    generator._flatten_elements = lambda *args, **kwargs: [{"name": "R1", "type": "Resistor", "nodes": ["1", "0"], "values": {}}]
    generator._remove_floating_from_flat = lambda flat: flat
    generator._build_graph_data = lambda flat: {"components": flat}

    result = await generator.gen_graph("* test")

    assert json.loads(result)["components"][0]["name"] == "R1"
    assert removed == ["temp.cir"]


@pytest.mark.asyncio
async def test_gen_graph_reraises_parser_errors_and_cleans_up(monkeypatch):
    removed = []
    printed = []

    class FakeTmp:
        name = "temp.cir"

        def write(self, code):
            return None

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

    class FailingParser:
        def __init__(self, path):
            raise RuntimeError("parse failed")

    monkeypatch.setattr(graph_module.tempfile, "NamedTemporaryFile", lambda **kwargs: FakeTmp())
    monkeypatch.setattr(graph_module, "SpiceParser", FailingParser)
    monkeypatch.setattr(graph_module.os, "remove", lambda path: removed.append(path))
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(args))

    with pytest.raises(RuntimeError):
        await GraphGenerator().gen_graph("* bad")

    assert removed == ["temp.cir"]
    assert any("ERROR parsing circuit" in str(args[0]) for args in printed)
