# Firmware

Embedded AI firmware for real-time cocoon detection, tracking, counting, and projected area estimation on the **Sipeed MaixCam**.

---

## Overview

This directory contains the complete firmware implementation of the Cocoon Detection and Area Estimation system.

The firmware captures images from the onboard camera, performs object detection using a custom-trained **YOLOv5** model, tracks detected cocoons with **ByteTrack**, estimates their projected area through blob analysis, counts cocoons crossing a predefined counting line, and displays the results using the MaixCam touchscreen interface.

The current implementation follows a modular software architecture that separates hardware initialization, application logic, image processing, configuration, and user interface rendering into independent modules.

---

## Features

- Real-time cocoon detection using YOLOv5
- Multi-object tracking using ByteTrack
- Projected area estimation using blob analysis
- Automatic cocoon counting
- Touchscreen-based graphical interface
- GPIO LED status indication
- Centralized configuration management
- Modular firmware architecture

---

## Directory Structure

```text
firmware/
│
├── README.md
├── cocoon_final2.py
├── main.py
├── hardware.py
├── config.py
├── area.py
├── ui.py
└── utils.py
```

---

## Module Description

### cocoon_final2.py

Original monolithic implementation of the firmware where the complete application logic is contained within a single file.

---

### main.py

Main application entry point.

Responsibilities:

- Initialize hardware
- Capture camera frames
- Execute YOLOv5 inference
- Update ByteTrack tracker
- Estimate cocoon area
- Count detected cocoons
- Render the graphical interface

---

### hardware.py

Initializes all hardware resources.

Includes:

- Camera
- Display
- Touchscreen
- YOLOv5 detector
- ByteTrack tracker
- GPIO status LED

---

### config.py

Stores configurable firmware parameters.

Examples include:

- Model path
- Confidence threshold
- IoU threshold
- Counting limit
- Counting line position
- Calibration constants
- Blob detection parameters
- User interface settings

---

### area.py

Performs projected cocoon area estimation.

Processing steps:

1. Crop object ROI
2. Perform blob detection
3. Find largest connected component
4. Calculate projected area
5. Return measured area

---

### ui.py

Contains all user interface rendering functions.

Responsible for:

- Drawing detection boxes
- Drawing counting line
- Displaying cocoon count
- Displaying projected area
- Drawing touchscreen exit button

---

### utils.py

Contains reusable helper functions shared across the firmware.

Current functionality includes:

- Touchscreen button detection

---

## Firmware Workflow

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
Display Output
```

---

## Software Architecture

```text
                    +----------------------+
                    |      main.py         |
                    | Application Control  |
                    +----------+-----------+
                               |
        +----------+-----------+-----------+-----------+
        |          |           |           |           |
        ▼          ▼           ▼           ▼           ▼
 hardware.py  config.py   area.py      ui.py     utils.py
        |                     |            |
        |                     |            |
        ▼                     ▼            ▼
 Hardware             Area Estimation   Rendering
 Initialization
```

---

## Runtime Sequence

1. Initialize hardware peripherals.
2. Capture a camera frame.
3. Perform YOLOv5 inference.
4. Track detected cocoons using ByteTrack.
5. Estimate projected area.
6. Count cocoons crossing the counting line.
7. Render the graphical interface.
8. Display the processed frame.
9. Repeat until the application exits.

---

## Dependencies

- MaixPy
- YOLOv5
- ByteTrack
- Maix Camera API
- Maix Display API
- Maix Touchscreen API

---

## Version Information

| Version | Description |
|----------|-------------|
| v1.0 | Original single-file firmware (`cocoon_final2.py`) |
| v1.1 | Modular firmware architecture (`main.py`, `hardware.py`, `config.py`, `area.py`, `ui.py`, `utils.py`) |

---

## Authors

- Revanth A H
- Parthavi N R
