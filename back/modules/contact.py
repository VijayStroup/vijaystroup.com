import os
import smtplib
from email.message import EmailMessage


def send_mail(name, email, message):
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))

            msg = EmailMessage()
            msg['Subject'] = f'vijaystroup.com | {name} - {email}'
            msg['From'] = os.getenv('EMAIL_USER')
            msg['To'] = 'vijay@vijaystroup.com'
            msg.set_content(message)

            smtp.send_message(msg)
        return 0
    except:
        return 1
