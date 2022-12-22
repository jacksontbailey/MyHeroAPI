from core.background import send_email
from core.security_funct import generate_verification_token
from db.repository.token import mark_as_verified, is_valid_verification_token, save_verification_token
from email.message import EmailMessage
from fastapi import BackgroundTasks, APIRouter

# https://fastapi.tiangolo.com/tutorial/background-tasks/
router = APIRouter()

@router.post("/request")
def send_verification_email(email: str, background_tasks: BackgroundTasks):
    # Generate the verification token
    token = generate_verification_token(email)

    # Save the verification token to the database
    save_verification_token(email, token)

    # Compose the email message
    message = EmailMessage()
    message["Subject"] = "Verify Your Account"
    message["From"] = "noreply@example.com"
    message["To"] = email
    message.set_content(
        f"Please click the following link to verify your account: "
        f"http://example.com/verify?email={email}&token={token}"
    )

    # Send the email in the background
    background_tasks.add_task(send_email, message)

    # Add the send email task to the list of background tasks
    #background_tasks.add_task(create_message, to=email, subject="Verify your account", message_text =f"Please click on the following link to verify your account: {verification_link}")

@router.get("/verify")
def verify(email: str, token: str):
    # Validate the token
    if not is_valid_verification_token(email, token):
        return {"error": "Invalid token"}

    # Mark the user as verified
    mark_as_verified(email)
    return {"message": "Successfully verified"}