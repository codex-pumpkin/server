import asyncio
from pathlib import Path

import pytest

from src.persistence.impl.validator.CodeValidator import CodeValidator


class FakeProcess:
    def __init__(self, returncode=0, stdout=b"", stderr=b""):
        self.returncode = returncode
        self._stdout = stdout
        self._stderr = stderr
        self.killed = False
        self.waited = False

    async def communicate(self):
        return self._stdout, self._stderr

    def kill(self):
        self.killed = True

    async def wait(self):
        self.waited = True


@pytest.mark.asyncio
async def test_validate_code_reads_ngspice_output(monkeypatch):
    created_output = {}

    async def fake_exec(*args, **kwargs):
        out_path = Path(args[3])
        out_path.write_text("file output", encoding="utf-8")
        created_output["path"] = out_path
        return FakeProcess(returncode=0, stdout=b"stdout", stderr=b"stderr")

    async def fake_wait_for(awaitable, timeout):
        return await awaitable

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
    monkeypatch.setattr(asyncio, "wait_for", fake_wait_for)

    result = await CodeValidator().validate_code("* test\n.end")

    assert result.isValid is True
    assert result.exitCode == 0
    assert "file output" in result.rawOutput
    assert "stdoutstderr" in result.rawOutput
    assert not created_output["path"].exists()


@pytest.mark.asyncio
async def test_validate_code_timeout_kills_process(monkeypatch):
    process = FakeProcess(returncode=124)

    async def fake_exec(*args, **kwargs):
        return process

    async def fake_wait_for(awaitable, timeout):
        raise asyncio.TimeoutError

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
    monkeypatch.setattr(asyncio, "wait_for", fake_wait_for)

    result = await CodeValidator().validate_code("* test\n.end")

    assert result.isValid is True
    assert result.exitCode == 124
    assert result.rawOutput == "Simulation timed out"
    assert process.killed is True
    assert process.waited is True


@pytest.mark.asyncio
async def test_validate_code_handles_missing_ngspice(monkeypatch):
    async def fake_exec(*args, **kwargs):
        raise FileNotFoundError

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)

    result = await CodeValidator().validate_code("* test\n.end")

    assert result.isValid is False
    assert result.exitCode == -1
    assert "ngspice not found" in result.rawOutput


@pytest.mark.asyncio
async def test_validate_code_handles_unexpected_error(monkeypatch):
    async def fake_exec(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)

    result = await CodeValidator().validate_code("* test\n.end")

    assert result.isValid is False
    assert result.exitCode == -2
    assert "boom" in result.rawOutput
