import asyncio
import ssl
import aiosmtplib
from email.message import EmailMessage
from src.core import settings as default_settings
from src.core import MailSettings
from src.persistence.interfaces import IMailSender

class MailSender(IMailSender):
    def __init__(self, settings:MailSettings):
        self.context:ssl.SSLContext = ssl.create_default_context()
        self.settings:MailSettings = settings

    async def _send_email(self, to_email: str, subject: str, html_content: str) -> None:
        """Generic async HTML email sender"""
        message = EmailMessage()
        message["From"] = self.settings.app_mail
        message["To"] = to_email
        message["Subject"] = subject
        message.set_content("This email requires an HTML-capable client.")
        message.add_alternative(html_content, subtype="html")

        await aiosmtplib.send(
            message,
            hostname=self.settings.smtp_server,
            port=self.settings.port,
            username=self.settings.app_mail,
            password=self.settings.password,
            use_tls=True,
            timeout=20,
        )

    async def send_confirmation_email(self, to_email: str, confirmation_code: str) -> None:
        """async Email confirmation sender"""
        subject = f"Your CodeX confirmation code is {confirmation_code}"
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #222; text-align: center; background-color: #fafafa; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                    <img src="{self.settings.logo}" alt="CodeX Logo" style="width: 120px; margin-bottom: 15px; border-radius: 10%;">
                    <h2 style="color: #ff6600;">Welcome to <b>CodeX</b></h2>
                    <p>Dear Innovator,</p>
                    <p>
                        Welcome to <b style="color: #ff6600;">CodeX</b> — where natural language meets intelligent code generation!<br>
                        Please confirm your email using the code below:
                    </p>
                    <p style="font-size: 1.3em; background: #fff3e6; padding: 12px 18px; border-radius: 6px; display: inline-block;">
                        <b>Confirmation Code:</b> {confirmation_code}
                    </p>
                    <p>
                        Enter this code in the application to verify your account.<br><br>
                        If you didn’t request this verification, you can safely ignore this message.
                    </p>
                    <hr style="border:none; border-top:1px solid #eee; margin:20px 0;">
                    <p>Best regards,<br>
                    <b style="color:#ff6600;">The CodeX Team</b><br>
                    </p>
                </div>
            </body>
        </html>
        """
        await self._send_email(to_email, subject, html_content)

    async def send_password_reset_email(self, to_email: str, reset_link: str) -> None:
        subject = "CodeX Password Reset Request"
        html_content = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #222; text-align: center; background-color: #fafafa; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background: #fff; border-radius: 10px; padding: 20px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                    <img src="{self.settings.logo}" alt="CodeX Logo" style="width: 120px; margin-bottom: 15px; border-radius: 10%;">
                    <h2 style="color: #ff6600;">Password Reset Request</h2>
                    <p>Dear Innovator,</p>
                    <p>
                        We received a request to reset the password for your <b style="color: #ff6600;">CodeX</b> account.<br>
                        To set a new password, please click the button below:
                    </p>
                    <p>
                        <a href="{reset_link}" style="background-color: #ff6600; color: white; padding: 12px 25px; text-decoration: none; border-radius: 8px; font-weight: bold;">
                            Reset Password
                        </a>
                    </p>
                    <p>
                        This link will expire in <b>30 minutes</b> for your security.<br>
                        If you didn’t request this password reset, you can safely ignore this email.
                    </p>
                    <hr style="border:none; border-top:1px solid #eee; margin:20px 0;">
                    <p>Best regards,<br>
                    <b style="color:#ff6600;">The CodeX Team</b><br>
                    </p>
                </div>
            </body>
        </html>
        """
        await self._send_email(to_email, subject, html_content)



async def main():
    mailer = MailSender(default_settings.mail_settings)
    await mailer.send_confirmation_email("lublusosku@gmail.com", "123456")
    await asyncio.sleep(1)
    await mailer.send_password_reset_email("lublusosku@gmail.com", "https://codex.com/reset-password")


if __name__ == "__main__":
    asyncio.run(main())
