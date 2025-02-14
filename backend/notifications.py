from twilio.rest import Client

# Twilio Credentials
TWILIO_ACCOUNT_SID = "ACfc4efd2fdd181f4550b9befe300f691e"
TWILIO_AUTH_TOKEN = "19018c40938d8962fa6efc469ce8591d"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio Sandbox Number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_notification(user_whatsapp):
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,  # Must be Twilio Sandbox Number
        body="🚀 Reminder: Please submit your form!",
        to=f"whatsapp:{user_whatsapp}"
    )
    print(f"WhatsApp Reminder sent to {user_whatsapp}")

# Test with a registered number
send_whatsapp_notification("whatsapp:+917402262339")  # Your registered number
