from picturepyfect.rotate_pyfect import rotate_pyfect
import numpy as np
import pytest

# Generate random images for testing
np.random.seed(42)
test_image = np.random.rand(3, 4, 5)
test_image_1 = rotate_pyfect(test_image, 1)
test_image_2 = rotate_pyfect(test_image, 2)
test_image_3 = rotate_pyfect(test_image, 3)
test_image_4 = rotate_pyfect(test_image, 4)

# test error handling
def test_error():
    with pytest.raises(TypeError):
        rotate_pyfect(None, 1)
    with pytest.raises(TypeError):
        rotate_pyfect(1, 1)
    with pytest.raises(TypeError):
        rotate_pyfect([1], 1)
    with pytest.raises(TypeError):
        rotate_pyfect("string", 1)


# test rotation_pyfect returned dimensions
def test_image_dimensions():
    assert test_image_1.shape == (3, 5, 4)
    assert test_image_2.shape == (3, 4, 5)
    assert test_image_3.shape == (3, 5, 4)
    assert test_image_4.shape == (3, 4, 5)


# test we don't lose any pixel values
def test_image_content():
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_1[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_1[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_1[0].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_1[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_1[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_1[1].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_1[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_1[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_1[2].flatten()), 10
    )

    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_2[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_2[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_2[0].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_2[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_2[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_2[1].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_2[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_2[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_2[2].flatten()), 10
    )

    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_3[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_3[0].flatten()), 10
    )
    assert round(sum(test_image[0].flatten()), 10) == round(
        sum(test_image_3[0].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_3[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_3[1].flatten()), 10
    )
    assert round(sum(test_image[1].flatten()), 10) == round(
        sum(test_image_3[1].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_3[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_3[2].flatten()), 10
    )
    assert round(sum(test_image[2].flatten()), 10) == round(
        sum(test_image_3[2].flatten()), 10
    )


# test that we don't the rows match the columns after rotation
def test_rows_cols():
    assert (test_image[0, 0, :] == test_image_1[0, :, -1]).all()
    assert (test_image[0, 0, :] == test_image_2[0, -1, :][::-1]).all()
    assert (test_image[0, 0, :] == test_image_3[0, :, 0][::-1]).all()
    assert (test_image[0, 0, :] == test_image_4[0, 0, :]).all()
    assert (test_image[1, 0, :] == test_image_1[1, :, -1]).all()
    assert (test_image[1, 0, :] == test_image_2[1, -1, :][::-1]).all()
    assert (test_image[1, 0, :] == test_image_3[1, :, 0][::-1]).all()
    assert (test_image[1, 0, :] == test_image_4[1, 0, :]).all()
    assert (test_image[2, 0, :] == test_image_1[2, :, -1]).all()
    assert (test_image[2, 0, :] == test_image_2[2, -1, :][::-1]).all()
    assert (test_image[2, 0, :] == test_image_3[2, :, 0][::-1]).all()
    assert (test_image[2, 0, :] == test_image_4[2, 0, :]).all()
