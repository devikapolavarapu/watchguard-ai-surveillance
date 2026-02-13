import os
import threading
from twilio.rest import Client

def send_alert_async(message, image_url=None):
    def _send():
        sid = os.getenv("TWILIO_ACCOUNT_SID")
        token = os.getenv("TWILIO_AUTH_TOKEN")
        from_ = os.getenv("TWILIO_FROM")
        to_ = os.getenv("TWILIO_TO")

        if not all([sid, token, from_, to_]):
            print("[alerts] Twilio not configured, skip SMS.")
            return

        client = Client(sid, token)

        final_message = message
        if image_url:
            final_message += f"\n📸 Evidence: {image_url}"

        client.messages.create(
            body=final_message,
            from_=from_,
            to=to_
        )

        print("📩 SMS sent")

    threading.Thread(target=_send, daemon=True).start()
