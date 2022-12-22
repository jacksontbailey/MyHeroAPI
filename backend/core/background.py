import ssl
import smtplib
from core.config import ginfo
from email.message import EmailMessage


def send_email(message: EmailMessage):
    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("your-email@example.com", "your-password")

        # Send the email
        smtp.send_message(message)


#email_sender = ginfo.INFO['email_sender']
#email_password = ginfo.INFO['email_password']
#user_from = ginfo.INFO['sender_name']
#
#
#def create_message(to, subject, message_text):
#    message = EmailMessage()
#    message['From'] = email_sender
#    message['To'] = to
#    message['Subject'] = subject
#    message.set_content(message_text)
#    
#    context = ssl.create_default_context()
#
#    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#        smtp.login(email_sender, email_password)
#        smtp.sendmail(email_sender, to, message.as_string())