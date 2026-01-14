import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "codex.mail.kit@gmail.com"
receiver_email = "lublusosku@gmail.com"
password = "qmgp zach rxny otbs"

context = ssl.create_default_context()

class MailSender:
    def send_password_reset(self, reset_link: str) -> None:
        subject = "CodeX Password Reset Request"
        body = f"""\
Dear Innovator,

We received a request to reset the password for your CodeX account.

To set a new password, please click the link below (or copy it into your browser):

 Reset Password: {reset_link}

This link will expire in 30 minutes for your security.  
If you didn’t request this password reset, you can safely ignore this message—your account will remain secure.

Best regards,  
The CodeX Team  
"""

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def main() -> None:
    sender = MailSender()
    reset_link = "https://codex.com/reset-password"  # Replace with actual token or link
    sender.send_password_reset(reset_link)

if __name__ == "__main__":
    main()
