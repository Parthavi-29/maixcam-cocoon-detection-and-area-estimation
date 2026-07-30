# MaixCam Cocoon Detection and Area Estimation

An embedded AI system for **real-time cocoon detection, tracking, counting, and projected area estimation** on the **Sipeed MaixCam** using **YOLOv5** and **ByteTrack**.

---

## Overview

This project implements an embedded computer vision system for automated cocoon inspection on the Sipeed MaixCam platform.

The system captures live camera frames, detects cocoons using a custom-trained YOLOv5 model, tracks each cocoon with ByteTrack to prevent duplicate counting, estimates the projected area through blob analysis, and displays the results using the onboard touchscreen interface.

The project was developed using a modular firmware architecture to improve readability, maintainability, and future scalability.

---

## Features

- Real-time cocoon detection using YOLOv5
- Multi-object tracking using ByteTrack
- Automatic cocoon counting
- Projected area estimation using blob analysis
- Touchscreen graphical interface
- GPIO LED indication
- Modular firmware architecture
- Optimized for Sipeed MaixCam

---

## Hardware

- Sipeed MaixCam
- Integrated camera
- Touchscreen display
- GPIO LED

---

## Software Stack

- Python (MaixPy)
- YOLOv5
- ByteTrack
- Blob Analysis
- MaixHub

---

## Repository Structure

```text
maixcam-cocoon-detection-and-area-estimation/
│
├── firmware/
│   ├── README.md
│   ├── cocoon_final2.py
│   ├── main.py
│   ├── hardware.py
│   ├── config.py
│   ├── area.py
│   ├── ui.py
│   └── utils.py
│
├── images/
│
├── docs/
│
├── dataset/
│
├── models/
│
└── README.md
```

---

## System Workflow

```text
Camera
   │
   ▼
YOLOv5 Detection
   │
   ▼
ByteTrack Tracking
   │
   ▼
ROI Extraction
   │
   ▼
Blob Analysis
   │
   ▼
Projected Area Estimation
   │
   ▼
Cocoon Counting
   │
   ▼
GUI Rendering
   │
   ▼
Display
```

---

## Model Training

The object detection model was trained using **MaixHub** and deployed to the Sipeed MaixCam in `.mud` format.

Training workflow:

- Image collection
- Dataset annotation
- YOLOv5 training
- Model export
- Deployment on MaixCam

---

## Firmware

The complete firmware implementation is located in the `firmware/` directory.

The firmware includes:

- Hardware initialization
- Real-time object detection
- Object tracking
- Area estimation
- User interface rendering
- Configuration management

---

## Dataset

The cocoon dataset was created and annotated using the MaixHub platform.

The dataset is not included in this repository.

---

## Results

The firmware provides:

- Real-time cocoon detection
- Stable object tracking
- Projected area estimation
- Automatic cocoon counting
- Interactive touchscreen interface

> **Screenshots and demonstration images will be added to the `images/` directory.**

---

## Future Improvements

- Data logging
- Automatic calibration
- Wireless communication
- Remote monitoring
- Multi-class object detection
- Performance optimization

---

## Authors

- **Revanth A H**
- **Parthavi N R**

---

## License

This project is intended for academic and research purposes.
