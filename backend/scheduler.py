import schedule
import time
from main import send_notifications

# Schedule reminders daily at 10 AM
schedule.every().day.at("10:00").do(send_notifications)

while True:
    schedule.run_pending()
    time.sleep(60)
