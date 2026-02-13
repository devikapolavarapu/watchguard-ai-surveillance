import cv2
from ultralytics import YOLO
from app.threat_logic import assess_threat, confirm_detection
from app.utils import draw_box, save_evidence

model = YOLO("models/best.pt")

def run_detection():
    cap = cv2.VideoCapture(0)

    print("Weapon Detection – Intelligent Mode. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_area = frame.shape[0] * frame.shape[1]
        results = model(frame)

        for r in results:
            for box in r.boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = model.names[cls]

                if conf < 0.6:
                    continue

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                box_area = (x2 - x1) * (y2 - y1)
                threat = assess_threat(conf, box_area, frame_area)

                if confirm_detection(label):
                    save_evidence(frame, label, threat)

                draw_box(frame, (x1, y1, x2, y2), label, conf, threat)

        cv2.imshow("Weapon Detection - Intelligent Mode", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
