import cv2
import time
from collections import deque
from ultralytics import YOLO

from app.alerts import send_alert_async
from app.utils import save_evidence_image, upload_evidence_to_cloudinary

# ---------------------------------
# LOAD MODEL
# ---------------------------------
model = YOLO("models/best.pt")
print("MODEL CLASSES:", model.names)

# ---------------------------------
# CONFIG
# ---------------------------------
CONFIDENCE_THRESHOLD = 0.2

WINDOW_SIZE = 6
MIN_HITS_FOR_ALERT = 3
GLOBAL_ALERT_COOLDOWN = 10  # seconds

VALID_WEAPONS = [
    "gun", "knife", "pistol", "rifle", "handgun", "grenade"
]

# ---------------------------------
# CAMERA
# ---------------------------------
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

detection_window = deque(maxlen=WINDOW_SIZE)
weapon_present = False
last_alert_time = 0
weapon_start_time = None

print("⚖️ Weapon Detection (Context-Aware Risk System). Press 'q' to quit.")

# ---------------------------------
# MAIN LOOP
# ---------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_this_frame = False
    weapon_label = None

    results = model(frame, conf=CONFIDENCE_THRESHOLD, verbose=False)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id].lower()
            conf = float(box.conf[0])

            if label not in VALID_WEAPONS:
                continue

            detected_this_frame = True
            weapon_label = label

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            area = (x2 - x1) * (y2 - y1)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(
                frame,
                f"{label.upper()} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    detection_window.append(1 if detected_this_frame else 0)
    hit_count = sum(detection_window)

    now = time.time()

    # Track duration
    if detected_this_frame:
        if weapon_start_time is None:
            weapon_start_time = now
    else:
        weapon_start_time = None

    duration = int(now - weapon_start_time) if weapon_start_time else 0

    # -------------------------------
    # RISK SCORE (INTELLIGENT PART)
    # -------------------------------
    risk_score = 0
    risk_score += min(hit_count * 12, 40)
    risk_score += min(duration * 6, 40)

    if risk_score >= 70:
        risk_level = "CRITICAL"
    elif risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    # -------------------------------
    # ALERT LOGIC
    # -------------------------------
    if hit_count >= MIN_HITS_FOR_ALERT and not weapon_present:
        if now - last_alert_time > GLOBAL_ALERT_COOLDOWN:
            print(f"🚨 {risk_level} RISK ({risk_score}/100): {weapon_label.upper()}")

            image_path = save_evidence_image(frame, weapon_label.upper(), risk_level)
            image_url = upload_evidence_to_cloudinary(
                image_path, weapon_label.upper(), risk_level
            )

            send_alert_async(
                f"🚨 {risk_level} RISK ({risk_score}/100): "
                f"{weapon_label.upper()} visible for {duration}s",
                image_url=image_url
            )

            last_alert_time = now
            weapon_present = True

    if hit_count == 0:
        weapon_present = False

    cv2.imshow("Weapon Detection - Context Aware", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("🛑 Program exited cleanly.")
