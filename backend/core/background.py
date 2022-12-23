import smtplib
import ssl
from core.security_funct import generate_verification_token
from core.config import ginfo
from db.repository.token import save_verification_token
from email.message import EmailMessage
from fastapi import BackgroundTasks


def send_verification_email(email: str):
    # Generate the verification token
    token = generate_verification_token(email)

    # Save the verification token to the database
    save_verification_token(email, token)
    
    # Generate the text and styling of the email
    message = generate_verification_email(email=email, verification_token=token, host="localhost:3000")

    # Send the email in the background
    send_email(message)


def generate_verification_email(email: str, verification_token: str, host: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = "Verify Your Account"
    message["From"] = ginfo.INFO['email_sender']
    message["To"] = email
    
    # Generate the verification link
    verification_link = f"http://{host}/verify?token={verification_token}&email={email}"

    # Set the HTML content of the email
    message.set_content(f'''\
    <html>
        <body>
            <p>Thanks for signing up!</p>
            <p>Please verify your email address by clicking the button below:</p>
            <a href="{verification_link}" style="padding: 8px 12px; background-color: #3498db; color: white; border-radius: 4px; text-decoration: none;">Verify Email</a>
        </body>
    </html>
    ''', subtype='html')

    return message



def send_email(message: EmailMessage):
    # Connect to the SMTP server
    print(message)
    context= ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(ginfo.INFO['email_sender'], ginfo.INFO['email_password'])

        # Send the email
        smtp.send_message(message)