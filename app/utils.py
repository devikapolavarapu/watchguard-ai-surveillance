import os
import cv2
from datetime import datetime

import cloudinary
import cloudinary.uploader

# ---------------------------------
# CLOUDINARY CONFIG (reads from env)
# ---------------------------------
cloudinary.config(secure=True)

def save_evidence_image(frame, weapon_label, risk_level):
    os.makedirs("evidence", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{weapon_label}_{risk_level}_{timestamp}.jpg"
    filepath = os.path.join("evidence", filename)

    cv2.imwrite(filepath, frame)
    return filepath


def upload_evidence_to_cloudinary(image_path, weapon_label, risk_level):
    try:
        response = cloudinary.uploader.upload(
            image_path,
            folder="weapon_alerts",
            public_id=f"{weapon_label}_{risk_level}_{int(datetime.now().timestamp())}",
            overwrite=True
        )
        return response.get("secure_url")
    except Exception as e:
        print("[cloudinary] Upload failed:", e)
        return None
