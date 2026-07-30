"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    User interface rendering functions for the
    Cocoon Counter firmware.

Copyright (c) 2026
"""

from maix import image

from config import (
    EXIT_BUTTON_TEXT,
    EXIT_BUTTON_POS,
    COUNT_TEXT_POSITION,
    FINAL_AREA_POSITION_OFFSET,
    COUNT_LINE_RATIO,
)


def draw_exit_button(img):
    """
    Draw the touchscreen exit button.
    """

    img.draw_rect(
        EXIT_BUTTON_POS[0],
        EXIT_BUTTON_POS[1],
        EXIT_BUTTON_POS[2],
        EXIT_BUTTON_POS[3],
        image.COLOR_RED,
        2,
    )

    img.draw_string(
        EXIT_BUTTON_POS[0] + 5,
        EXIT_BUTTON_POS[1] + 10,
        EXIT_BUTTON_TEXT,
        image.COLOR_RED,
    )


def draw_count_line(img, camera):
    """
    Draw the counting line.

    Returns
    -------
    int
        Y-coordinate of the counting line.
    """

    count_line_y = int(camera.height() * COUNT_LINE_RATIO)

    img.draw_line(
        0,
        count_line_y,
        camera.width(),
        count_line_y,
        image.COLOR_YELLOW,
        2,
    )

    return count_line_y


def draw_detection_box(img, obj):
    """
    Draw a detected cocoon bounding box.
    """

    img.draw_rect(
        obj.x,
        obj.y,
        obj.w,
        obj.h,
        image.COLOR_RED,
    )


def draw_area_label(img, x, y, area):
    """
    Display the estimated cocoon area.
    """

    img.draw_string(
        x,
        y - 10,
        f"A:{area:.2f}cm2",
        image.COLOR_GREEN,
    )


def draw_final_area(img, camera, area):
    """
    Display the most recently counted cocoon area.
    """

    img.draw_string(
        camera.width() - FINAL_AREA_POSITION_OFFSET,
        10,
        f"A:{area:.2f}",
        image.COLOR_GREEN,
    )


def draw_count(img, count):
    """
    Display the cocoon count.
    """

    img.draw_string(
        COUNT_TEXT_POSITION[0],
        COUNT_TEXT_POSITION[1],
        f"Count:{count}",
        image.COLOR_GREEN,
        scale=2,
    )