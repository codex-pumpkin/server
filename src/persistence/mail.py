import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "codex.mail.kit@gmail.com"  # Enter your address
receiver_email = "lublusosku@gmail.com"  # Enter receiver address
password = "qmgp zach rxny otbs"


context = ssl.create_default_context()

class MailSender:

    def send_email(self, confirmation_code:str) -> None:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, f"Your confirmation code is {confirmation_code}")


def main() -> None:
    sender = MailSender()
    sender.send_email("1245")

if __name__ == "__main__":
    main()