"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Central configuration file containing application
    constants used throughout the firmware.

Copyright (c) 2026
"""

# ---------------------------------------------------------
# Model
# ---------------------------------------------------------

MODEL_PATH = "/root/cocoon/cocoonp2.maixcam/cocoon.mud"

# ---------------------------------------------------------
# Detection
# ---------------------------------------------------------

CONF_THRESHOLD = 0.50
IOU_THRESHOLD = 0.45

# ---------------------------------------------------------
# Tracking
# ---------------------------------------------------------

COUNT_LIMIT = 100

# Counting line position (50% of image height)
COUNT_LINE_RATIO = 0.5

# ---------------------------------------------------------
# Area Estimation
# ---------------------------------------------------------

CM_PER_PIXEL = 0.05

AREA_OFFSET = 3.0

# Blob detection parameters
BLOB_THRESHOLD = [(60, 255)]
BLOB_PIXEL_THRESHOLD = 50

# ---------------------------------------------------------
# Hardware
# ---------------------------------------------------------

LED_PIN = "A0"

# ---------------------------------------------------------
# User Interface
# ---------------------------------------------------------

EXIT_BUTTON_TEXT = "< EXIT"

EXIT_BUTTON_POS = [0, 0, 80, 40]

COUNT_TEXT_POSITION = (10, 80)

FINAL_AREA_POSITION_OFFSET = 120