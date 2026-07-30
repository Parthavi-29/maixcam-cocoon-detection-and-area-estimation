"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Main application for real-time cocoon counting
    and projected area estimation using YOLOv5 and
    ByteTrack.

Copyright (c) 2026
"""

from maix import (
    app,
    tracker,
)

from config import (
    CONF_THRESHOLD,
    IOU_THRESHOLD,
    EXIT_BUTTON_POS,
)

from hardware import initialize_hardware
from utils import is_in_button
from area import estimate_area
from ui import (
    draw_exit_button,
    draw_count_line,
    draw_detection_box,
    draw_area_label,
    draw_final_area,
    draw_count,
)


def main():

    hw = initialize_hardware()

    # ---------------------------------------------------------
    # Runtime State
    # ---------------------------------------------------------

    count = 0
    counted_ids = set()
    final_area = 0.0

    while not app.need_exit():

        img = hw.camera.read()

        # -----------------------------------------
        # Touchscreen
        # -----------------------------------------

        x_t, y_t, pressed = hw.touchscreen.read()

        if pressed:

            if hw.display.width() != hw.camera.width():
                x_t = int(
                    x_t * hw.camera.width() / hw.display.width()
                )
                y_t = int(
                    y_t * hw.camera.height() / hw.display.height()
                )

            if is_in_button(
                x_t,
                y_t,
                EXIT_BUTTON_POS,
            ):
                print("EXIT pressed")
                app.set_exit_flag(True)

        # -----------------------------------------
        # Detection
        # -----------------------------------------

        detections = hw.detector.detect(
            img,
            conf_th=CONF_THRESHOLD,
            iou_th=IOU_THRESHOLD,
        )

        track_objects = [
        tracker.Object(
            obj.x,
            obj.y,
            obj.w,
            obj.h,
            obj.class_id,
            obj.score,
        )
        for obj in detections
                        ]
        
        tracks = hw.tracker.update(track_objects)

        # -----------------------------------------
        # Draw counting line
        # -----------------------------------------

        count_line_y = draw_count_line(
            img,
            hw.camera,
        )

        # -----------------------------------------
        # Process tracks
        # -----------------------------------------

        for track in tracks:

            if track.lost:
                continue

            obj = track.history[-1]

            center_y = obj.y + obj.h // 2

            draw_detection_box(img, obj)

            area, x, y = estimate_area(img, obj)

            if area is None:
                continue

            if (
                center_y > count_line_y
                and track.id not in counted_ids
            ):

                count += 1
                counted_ids.add(track.id)

                final_area = area

                print(
                    "Cocoon:",
                    count,
                    "| Area:",
                    round(area, 2),
                    "cm^2",
                )

                if count == 100:

                    hw.led.value(1)
                    app.sleep_ms(1000)
                    hw.led.value(0)

                    count = 0
                    counted_ids.clear()

            draw_area_label(
                img,
                x,
                y,
                area,
            )

        # -----------------------------------------
        # UI
        # -----------------------------------------

        draw_exit_button(img)

        draw_final_area(
            img,
            hw.camera,
            final_area,
        )

        draw_count(
            img,
            count,
        )

        hw.display.show(img)


if __name__ == "__main__":
    main()