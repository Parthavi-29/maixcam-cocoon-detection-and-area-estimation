"""
Cocoon Counter with Area Estimation

Author(s):
    Revanth A H
    Parthavi N R

Description:
    Utility functions used throughout the
    Cocoon Counter firmware.

Copyright (c) 2026
"""


def is_in_button(x, y, button):
    """
    Check whether a point lies inside a rectangular button.

    Parameters
    ----------
    x : int
        X-coordinate.

    y : int
        Y-coordinate.

    button : list
        Rectangle defined as [x, y, width, height].

    Returns
    -------
    bool
        True if the point lies inside the button,
        otherwise False.
    """

    return (
        button[0] < x < button[0] + button[2]
        and button[1] < y < button[1] + button[3]
    )