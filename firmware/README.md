# Firmware

Embedded AI firmware for real-time cocoon detection, tracking, counting, and projected area estimation on the **Sipeed MaixCam**.

---

## Overview

This directory contains the firmware source code for the cocoon detection and area estimation system.

The firmware captures images from the onboard camera, performs object detection using a custom-trained **YOLOv5** model, tracks detected cocoons using **ByteTrack**, estimates projected cocoon area through blob analysis, counts cocoons crossing a predefined counting line, and displays the results through the MaixCam graphical interface.

The implementation follows a modular software architecture where hardware initialization, configuration, image processing, application logic, and user interface rendering are organized into separate modules.

---

## Features

- Real-time cocoon detection
- ByteTrack-based object tracking
- Projected area estimation
- Automatic cocoon counting
- Touchscreen user interface
- GPIO LED indication
- Modular firmware design

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

Original monolithic implementation of the complete firmware.

### main.py

Main application that controls the complete execution flow.

### hardware.py

Initializes the camera, display, touchscreen, YOLOv5 detector, ByteTrack tracker, and GPIO LED.

### config.py

Stores configurable parameters such as model path, thresholds, calibration constants, and UI settings.

### area.py

Performs projected area estimation using blob analysis.

### ui.py

Contains graphical interface rendering functions.

### utils.py

Contains helper functions used throughout the firmware.

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
Display
```

---

## Software Dependencies

- MaixPy
- YOLOv5
- ByteTrack

---

## Authors

- Revanth A H
- Parthavi N R
