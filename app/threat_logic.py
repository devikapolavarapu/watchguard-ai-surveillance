from collections import deque

FRAME_CONFIRMATION = 3
CONF_THRESHOLD = 0.6

history = deque(maxlen=FRAME_CONFIRMATION)

def assess_threat(conf, box_area, frame_area):
    if conf > 0.85 and box_area > 0.15 * frame_area:
        return "HIGH"
    return "MEDIUM"

def confirm_detection(label):
    history.append(label)
    return history.count(label) == FRAME_CONFIRMATION
