import importlib
from types import SimpleNamespace

import pytest

mail_module = importlib.import_module("src.persistence.impl.mail.MailSender")
MailSender = mail_module.MailSender


@pytest.mark.asyncio
async def test_send_email_builds_html_message(monkeypatch):
    sent = {}

    async def fake_send(message, **kwargs):
        sent["message"] = message
        sent["kwargs"] = kwargs

    settings = SimpleNamespace(
        app_mail="noreply@example.com",
        smtp_server="smtp.example.com",
        port=465,
        password="secret",
        logo="https://example.com/logo.png",
        client_base_url="http://localhost:8080",
    )

    monkeypatch.setattr(mail_module.aiosmtplib, "send", fake_send)

    sender = MailSender(settings)
    await sender._send_email("user@example.com", "Subject", "<b>Hello</b>")

    assert sent["message"]["From"] == "noreply@example.com"
    assert sent["message"]["To"] == "user@example.com"
    assert sent["message"]["Subject"] == "Subject"
    assert sent["kwargs"]["hostname"] == "smtp.example.com"
    assert "Hello" in sent["message"].as_string()


@pytest.mark.asyncio
async def test_send_email_swallows_transport_errors(monkeypatch):
    async def fake_send(*args, **kwargs):
        raise RuntimeError("smtp down")

    monkeypatch.setattr(mail_module.aiosmtplib, "send", fake_send)
    settings = SimpleNamespace(
        app_mail="noreply@example.com",
        smtp_server="smtp.example.com",
        port=465,
        password="secret",
        logo="https://example.com/logo.png",
        client_base_url="http://localhost:8080",
    )

    sender = MailSender(settings)
    await sender._send_email("user@example.com", "Subject", "<b>Hello</b>")


@pytest.mark.asyncio
async def test_mail_templates_delegate_to_send_email(monkeypatch):
    calls = []
    settings = SimpleNamespace(
        app_mail="noreply@example.com",
        smtp_server="smtp.example.com",
        port=465,
        password="secret",
        logo="https://example.com/logo.png",
        client_base_url="http://localhost:8080",
    )
    sender = MailSender(settings)

    async def fake_send_email(to_email, subject, html_content):
        calls.append((to_email, subject, html_content))

    monkeypatch.setattr(sender, "_send_email", fake_send_email)

    await sender.send_confirmation_email("user@example.com", "123456")
    await sender.send_password_reset_email("user@example.com", "654321")
    await sender.send_temporary_password_email("user@example.com", "temp-pass")

    assert calls[0][1] == "Your CodeX confirmation code is 123456"
    assert "/email-verification/123456" in calls[0][2]
    assert calls[1][1] == "CodeX Password Reset Code"
    assert "/reset-password/654321" in calls[1][2]
    assert calls[2][1] == "CodeX Password"
    assert "temp-pass" in calls[2][2]
