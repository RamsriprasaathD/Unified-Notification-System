from fastapi import FastAPI
from google_sheets import get_submitted_users
from notifications import send_whatsapp_notification
from users import registered_users
import scheduler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "UCNMS API Running"}

@app.get("/get_pending_users/")
def get_pending_users():
    submitted_users = get_submitted_users()
    pending_users = [user for user in registered_users if user not in submitted_users]
    return {"pending_users": pending_users}

@app.post("/send_notifications/")
def send_notifications():
    pending_users = get_pending_users()["pending_users"]
    for user in pending_users:
        send_whatsapp_notification(user)
    return {"status": "Notifications sent"}
