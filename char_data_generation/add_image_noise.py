"""
Add noise to an image.

Take a given image, add noise to the image (blur, rotation,
salt and pepper noise, and perspective change) and output the
noisey image.
"""


from PIL import Image, ImageFilter
import numpy as np
from random import uniform
import sys
import os


def add_rotation(image, max_degrees=2):
    """Rotate an image up to a maximum of 2 degrees in either direction."""
    rand_degr = uniform(-max_degrees, max_degrees)
    return image.rotate(rand_degr)


def add_s_and_p(image, mean_amount=0.004):
    """Add salt and pepper noise to on average 0.4% of the pixels."""
    image = image.convert('LA')  # convert to greyscale
    image = np.array(image)
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = uniform(mean_amount-0.001, mean_amount+0.001)
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[tuple(coords)] = 1

    # Pepper mode
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[tuple(coords)] = 0

    out = Image.fromarray(out).convert('RGB')
    return out


def add_perspective_noise(image, max_slope=0.05):
    """
    Return an image with a perspective rotation.

    The default range of slopes that can be chosen for the rotation is
    between -0.05 and 0.05.
    """
    width, height = image.size
    m = uniform(-max_slope, max_slope)
    xshift = abs(m) * width
    new_width = width + int(round(xshift))
    image = image.transform((new_width, height), Image.AFFINE,
                            (1, m, -xshift if m > 0 else 0, 0, 1, 0),
                            Image.BICUBIC)
    return image


def add_noise(image):
    """
    Return an image with added noise.

    The added noise includes blur, rotation, salt and pepper noise,
    and perspective change.
    """
    image = image.filter(ImageFilter.BLUR)  # add blur
    image = add_rotation(image)
    image = add_s_and_p(image)
    image = add_perspective_noise(image)
    return image


def get_absolute_path(relative_path):
    """
    Get the absolute file path to a desired file.

    Parameters:
        relative_path --> a string with the path to a file relative to the
                          current directory
                          Example: "../char_data_generation/random_chars.txt"

    Returns:
        A string with the absolute file path to a given file.

    """
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def main():
    """
    Run to add noise to a specified image.

    USAGE: Supply a single argument - the image to add noise to.
    Example: > python3 add_image_noise.py test_data.tif
    """
    image_name = sys.argv[1]  # the image path
    image = Image.open(image_name).convert('RGB')
    image = add_noise(image)

    image_name = os.path.basename(image_name)  # extract the file name only
    new_image_name = image_name[:-4]  # strip of .tif
    new_image_name += ".png"  # png for smaller file size
    path = get_absolute_path("noisey_font_images/") + new_image_name

    image.save(path, dpi=(70, 70))


if __name__ == "__main__":
    main()
