import smtplib
import ssl
from core.security_funct import generate_token
from core.config import ginfo, settings
from db.repository.token import save_token
from email.message import EmailMessage

def generate_link(host: str, token: str, email: str, endpoint: str) -> str:
    return f"{host}/{endpoint}?token={token}&email={email}"

def generate_email(subject: str, html_content: str, email: str, token: str, host: str, endpoint: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = ginfo.INFO['email_sender']
    message["To"] = email
    
    # Generate the verification link
    clickable_link = generate_link(host, token, email, endpoint)

    # Set the HTML content of the email
    message.set_content(html_content.format(clickable_link=clickable_link), subtype='html')
    
    return message

def send_email(message: EmailMessage):
    # Connect to the SMTP server
    context= ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(ginfo.INFO['email_sender'], ginfo.INFO['email_password'])

        # Send the email
        smtp.send_message(message)


def send_token_email(email: str, host: str, token: str, collection: str, subject: str, html_content: str, endpoint: str):
    # Save the token to the database
    save_token(collection=collection, email=email, token=token)
    
    # Generate the text and styling of the email
    message = generate_email(
        subject=subject,
        html_content=html_content,
        email=email,
        token=token,
        host=host,
        endpoint=endpoint
    )

    # Send the email in the background
    send_email(message)

def send_verification_email(email: str, host: str):
    # Generate the verification token
    token = generate_token(email=email, secret=settings.JWT_VERFICATION_SECRET )

    # Send the verification email
    send_token_email(
        email=email,
        host=host,
        token=token,
        collection=settings.VERIFY_COLL,
        subject="Verify Your Account",
        html_content="""
        <html>
            <body>
                <p>Thanks for signing up!</p>
                <p>Please verify your email address by clicking the button below:</p>
                <a href={clickable_link} style="padding: 8px 12px; background-color: #3498db; color: white; border-radius: 4px; text-decoration: none;">Verify Email</a>
            </body>
        </html>
        """,
        endpoint="verify"
    )

def send_password_reset_email(email: str, host: str):
    # Generate the password reset token
    token = generate_token(email=email, secret=settings.JWT_PASSRESET_SECRET )

    # Send the password reset email
    send_token_email(
        email=email,
        host=host,
        token=token,
        collection=settings.PASSRESET_COLL,
        subject="Reset Your Password",
        html_content="""
        <html>
            <body>
                <p>We received a request to reset the password for your account.</p>
                <p>If you didn't make this request, you can ignore this email.</p>
                <p>To reset your password, click the button below:</p>
                <a href={clickable_link} style="padding: 8px 12px; background-color: #3498db; color: white; border-radius: 4px; text-decoration: none;">Reset Password</a>
            </body>
        </html>
        """,
        endpoint="reset-password"
    )        

