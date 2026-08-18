import numpy as np
import pytest

from src.image_preprocessing import crop_image, resize_image


def sample_image():
    return np.zeros((100, 120, 3), dtype=np.uint8)


def test_resize_shape():
    assert resize_image(sample_image(), 60, 40).shape == (40, 60, 3)


def test_resize_rejects_zero_width():
    with pytest.raises(ValueError):
        resize_image(sample_image(), 0, 40)


def test_resize_rejects_negative_height():
    with pytest.raises(ValueError):
        resize_image(sample_image(), 60, -1)


def test_resize_rejects_non_integer_dimension():
    with pytest.raises(TypeError):
        resize_image(sample_image(), 60.5, 40)


def test_resize_rejects_non_array():
    with pytest.raises(TypeError):
        resize_image("not-an-image", 60, 40)


def test_resize_rejects_empty_array():
    with pytest.raises(ValueError):
        resize_image(np.array([]), 60, 40)


def test_crop_shape():
    assert crop_image(sample_image(), 10, 20, 30, 40).shape == (40, 30, 3)


def test_crop_rejects_negative_coordinate():
    with pytest.raises(ValueError):
        crop_image(sample_image(), -1, 0, 30, 40)


def test_crop_rejects_out_of_bounds_width():
    with pytest.raises(ValueError):
        crop_image(sample_image(), 100, 0, 30, 40)


def test_crop_rejects_out_of_bounds_height():
    with pytest.raises(ValueError):
        crop_image(sample_image(), 0, 80, 30, 40)


def test_crop_returns_copy():
    image = sample_image()
    cropped = crop_image(image, 0, 0, 20, 20)
    cropped[:] = 255
    assert image[0, 0, 0] == 0
