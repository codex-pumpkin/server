import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "codex.mail.kit@gmail.com"
receiver_email = "lublusosku@gmail.com"
password = "qmgp zach rxny otbs"

context = ssl.create_default_context()

class MailSender:
    def send_email(self, confirmation_code: str) -> None:
        subject = f"Your CodeX confirmation code is {confirmation_code}"
        body = f"""\
Dear Innovator,

Welcome to the CodeX Project — where natural language meets intelligent code generation!  
To complete your registration and unlock full access, please confirm your email using the code below:

 Confirmation Code: {confirmation_code}

Enter this code in the application to verify your account.

If you didn’t request this verification, you can safely ignore this message.

Best regards,  
The CodeX Team  
"""

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def main() -> None:
    sender = MailSender()
    sender.send_email("1245")

if __name__ == "__main__":
    main()
