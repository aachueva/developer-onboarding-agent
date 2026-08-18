"""Small OpenCV-style wrapper used to demonstrate governed contributions."""

from __future__ import annotations

import cv2
import numpy as np


def _validate_image(image: np.ndarray) -> None:
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a numpy.ndarray")
    if image.size == 0:
        raise ValueError("image must not be empty")


def _validate_dimension(value: int, name: str) -> None:
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero")


def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    """Resize an image to an explicit width and height."""
    _validate_image(image)
    _validate_dimension(width, "width")
    _validate_dimension(height, "height")
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def crop_image(
    image: np.ndarray, x: int, y: int, width: int, height: int
) -> np.ndarray:
    """Crop an image after validating coordinates and dimensions."""
    _validate_image(image)
    for value, name in ((x, "x"), (y, "y")):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be non-negative")
    _validate_dimension(width, "width")
    _validate_dimension(height, "height")

    image_height, image_width = image.shape[:2]
    if x + width > image_width or y + height > image_height:
        raise ValueError("crop must fit within image bounds")
    return image[y : y + height, x : x + width].copy()
