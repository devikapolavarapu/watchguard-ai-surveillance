# 🚀 WatchGuard AI Surveillance

### Context-Aware AI Threat Detection & Intelligent Alerting System
---

## 📌 Overview

**WatchGuard AI** is a real-time, decision-aware surveillance system built to detect weapon threats and generate evidence-backed alerts using computer vision and contextual risk evaluation.

Unlike basic object detection demos, this system introduces:

- Temporal validation  
- Risk scoring (0–100 scale)  
- Severity classification  
- Automated evidence capture  
- Cloud-hosted proof storage  
- SMS alerting  
- Structured incident logging  

The objective is not just detection — but **intelligent threat confirmation with accountability**.

---

## 🧠 Problem Statement

Traditional AI detection systems often trigger alerts on single-frame detections, leading to:

- High false positives  
- Alert fatigue  
- Lack of contextual reasoning  
- No structured audit trail  

Real-world surveillance systems require a **decision engine layer**, not just detection.

---

## 🏗 System Architecture

    Camera Input
  
       ↓
    YOLO Detection Engine

       ↓
   
    Threat Logic Layer

       ↓
    Risk Scoring Engine

       ↓
    Temporal Confirmation

       ↓
  
    Evidence Capture

       ↓

    Cloud Upload


      ↓

    SMS Alert Dispatch

        ↓

    Incident Logging


---

## ⚙️ Core Features

### 🔍 Real-Time Weapon Detection
- YOLO-based inference pipeline
- Supports detection of:
  - Gun
  - Knife
  - Grenade
  - Rifle
  - Handgun
- Live webcam processing using OpenCV

---

### 🎯 Context-Aware Risk Scoring

Each confirmed detection is evaluated using:

- Model confidence score  
- Duration of object visibility  
- Temporal stability across frames  
- Cooldown validation logic  

Threat levels are categorized as:

| Risk Score | Severity Level |
|------------|---------------|
| 0–30       | LOW           |
| 31–60      | MEDIUM        |
| 61–80      | HIGH          |
| 81–100     | CRITICAL      |

---

### ⏳ Temporal Confirmation Engine

Alerts are NOT triggered on single-frame detections.

The system requires:
- Multi-frame validation  
- Minimum hit threshold  
- Cooldown control  

This significantly reduces false alarms.

---

### 📸 Automated Evidence Capture

On confirmed detection:
- Snapshot is saved locally
- Image is uploaded to cloud storage
- Secure public URL is generated
- URL is included in alert message

---

### ☁️ Cloud-Based Evidence Hosting

Images are uploaded via cloud API integration, enabling:

- Remote access  
- Secure sharing  
- Evidence documentation  

---

### 📩 SMS Alert System

Integrated with Twilio API to send:
![WhatsApp Image 2026-02-13 at 12 35 05 PM](https://github.com/user-attachments/assets/28c551f8-2967-4ce0-8e1a-a7c741fd616a)
<img width="328" height="738" alt="image" src="https://github.com/user-attachments/assets/25e84654-aa2f-447a-8baa-8be861d65ed3" />

🚨 HIGH RISK (72/100): GUN detected for 5 seconds
Evidence: https://res.cloudinary.com/dlh1nk6pq/image/upload/v1768937963/weapon_alerts/KNIFE_MEDIUM_1768937963.jpg
...


Alerts include:
- Weapon type
- Risk score
- Threat level
- Evidence URL

---

### 🧾 Incident Logging (Audit Trail)

Each confirmed threat is logged with:

- Timestamp  
- Weapon Type  
- Risk Score  
- Severity Level  
- Visibility Duration  
- Evidence URL  
- Source ID  

Enabling:
- Post-incident analysis  
- Pattern tracking  
- Reporting & documentation  

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- YOLOv8  
- Twilio API  
- Cloud Storage API  
- Modular Threat Logic Engine  

---

## 📁 Project Structure



app/
│

├── alerts.py # SMS alert handling

├── detector.py # YOLO inference engine

├── threat_logic.py # Risk scoring & decision logic

└── utils.py # Evidence capture & cloud upload


main.py # Orchestration layer

.gitignore

README.md


---

## 📈 Why This Project Stands Out

This is not a simple object detection demo.

It introduces:

- A dedicated decision engine  
- False positive mitigation strategy  
- Evidence-backed alerting  
- Structured audit logging  
- Modular and scalable architecture  

It simulates how real-world surveillance intelligence systems are engineered.

---

## 🔮 Future Enhancements

- AWS S3 enterprise storage integration  
- Multi-camera stream support  
- Web-based monitoring dashboard  
- Database-backed incident tracking  
- Edge deployment optimization  

---

## 👩‍💻 Author

Developed as an advanced AI surveillance system focusing on intelligent threat validation and production-level alert design.
  - Devika Polavarapu
## Collaborators

- Yeluguri Gnana Prasanna
- Pachipulusu Vyshnavi Annapurna
