from core.background import write_notification
from fastapi import BackgroundTasks, APIRouter

# https://fastapi.tiangolo.com/tutorial/background-tasks/
router = APIRouter()

@router.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message= "some notification")
    return {"message": "Notification sent in the background"}

