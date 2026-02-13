# WatchGuard AI Surveillance

Context-Aware AI Surveillance for Real-World Threat Detection

## Overview
WatchGuard is a decision-aware AI surveillance system designed to detect weapons in real time and generate evidence-backed alerts.

Unlike basic object detection demos, this system applies contextual risk scoring and temporal confirmation to reduce false alarms and improve alert reliability.

## Key Features
- Real-time weapon detection (YOLO-based)
- Risk scoring system (0–100)
- Threat classification (LOW / MEDIUM / HIGH / CRITICAL)
- Temporal confirmation to avoid false positives
- Automated evidence capture
- Cloud-hosted visual proof
- SMS alerts with clickable evidence links
- Incident logging (CSV audit trail)

## Architecture
Detection → Risk Engine → Decision Layer → Evidence Capture → Cloud Upload → Alerting → Incident Logging

## Tech Stack
Python · OpenCV · YOLOv8 · Twilio API · Cloudinary

## Future Scope
- Pluggable cloud storage (AWS S3 support)
- Multi-camera scaling
- Web dashboard for monitoring
