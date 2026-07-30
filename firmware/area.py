"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Functions for estimating cocoon projected area
    using blob analysis and calibration-based
    pixel-to-area conversion.

Copyright (c) 2026
"""

from config import (
    CM_PER_PIXEL,
    AREA_OFFSET,
    BLOB_THRESHOLD,
    BLOB_PIXEL_THRESHOLD,
)


def estimate_area(img, obj):
    """
    Estimate the projected area of a detected cocoon.

    Parameters
    ----------
    img
        Current camera frame.

    obj
        Detected or tracked object.

    Returns
    -------
    tuple
        (area_cm2, roi_x, roi_y)

        area_cm2 is None if estimation fails.
    """

    x = max(0, obj.x)
    y = max(0, obj.y)
    w = min(obj.w, img.width() - x)
    h = min(obj.h, img.height() - y)

    if w <= 0 or h <= 0:
        return None, x, y

    roi = img.crop(x, y, w, h)

    blobs = roi.find_blobs(
        BLOB_THRESHOLD,
        pixels_threshold=BLOB_PIXEL_THRESHOLD,
    )

    largest = max((blob.pixels() for blob in blobs), default=0)

    if largest == 0:
        return None, x, y

    area_cm2 = (
        largest * (CM_PER_PIXEL ** 2)
        - AREA_OFFSET
    )

    return area_cm2, x, y