"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Initializes and manages all hardware peripherals,
    including the camera, display, touchscreen,
    YOLOv5 detector, ByteTrack tracker,
    and status LED.

Copyright (c) 2026
"""

from dataclasses import dataclass

from maix import (
    camera,
    display,
    touchscreen,
    nn,
    tracker,
    gpio,
)

from config import (
    MODEL_PATH,
    LED_PIN,
)


@dataclass
class Hardware:
    """
    Container holding all initialized hardware interfaces.
    """

    detector: object
    camera: object
    display: object
    touchscreen: object
    tracker: object
    led: object


def initialize_hardware() -> Hardware:
    """
    Initialize all hardware required by the application.

    Returns
    -------
    Hardware
        Initialized hardware interfaces.
    """

    # ---------------------------------------------------------
    # YOLOv5 Detector
    # ---------------------------------------------------------

    detector = nn.YOLOv5(model=MODEL_PATH)

    # ---------------------------------------------------------
    # Camera
    # ---------------------------------------------------------

    cam = camera.Camera(
        detector.input_width(),
        detector.input_height(),
        detector.input_format(),
    )

    # ---------------------------------------------------------
    # Display
    # ---------------------------------------------------------

    disp = display.Display()

    # ---------------------------------------------------------
    # Touchscreen
    # ---------------------------------------------------------

    ts = touchscreen.TouchScreen()

    # ---------------------------------------------------------
    # ByteTrack
    # ---------------------------------------------------------

    tracker_instance = tracker.ByteTracker()

    # ---------------------------------------------------------
    # Status LED
    # ---------------------------------------------------------

    led = gpio.GPIO(LED_PIN, gpio.Mode.OUT)
    led.value(0)

    # ---------------------------------------------------------
    # Return Hardware Object
    # ---------------------------------------------------------

    return Hardware(
        detector=detector,
        camera=cam,
        display=disp,
        touchscreen=ts,
        tracker=tracker_instance,
        led=led,
    )