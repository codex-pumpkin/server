import asyncio
import importlib
import types


def test_tokens_and_hash_util_mains(monkeypatch):
    tokens_module = importlib.import_module("src.business.impl.auth.tokens")
    hash_module = importlib.import_module("src.persistence.impl.database.hash_util")

    printed = []
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(args))

    tokens_module._main()
    hash_module._main()

    assert printed


def test_mail_sender_main(monkeypatch):
    mail_module = importlib.import_module("src.persistence.impl.mail.MailSender")
    calls = []
    real_sleep = asyncio.sleep

    async def fake_confirmation(self, *args, **kwargs):
        calls.append("confirm")

    async def fake_reset(self, *args, **kwargs):
        calls.append("reset")

    async def fake_temp(self, *args, **kwargs):
        calls.append("temp")

    monkeypatch.setattr(mail_module.MailSender, "send_confirmation_email", fake_confirmation)
    monkeypatch.setattr(mail_module.MailSender, "send_password_reset_email", fake_reset)
    monkeypatch.setattr(mail_module.MailSender, "send_temporary_password_email", fake_temp)
    monkeypatch.setattr(asyncio, "sleep", lambda _: real_sleep(0))

    asyncio.run(mail_module.main())

    assert calls == ["confirm", "reset", "temp"]


def test_code_validator_main(monkeypatch):
    validator_module = importlib.import_module("src.persistence.impl.validator.CodeValidator")
    printed = []

    async def fake_validate(self, code):
        return types.SimpleNamespace(isValid=True, exitCode=0, rawOutput="ok")

    monkeypatch.setattr(validator_module.CodeValidator, "validate_code", fake_validate)
    monkeypatch.setattr("builtins.print", lambda *args, **kwargs: printed.append(args))

    asyncio.run(validator_module._main())

    assert any("Valid:" in str(args[0]) for args in printed)
