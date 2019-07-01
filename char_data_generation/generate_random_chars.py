"""
Generates n random characters and writes these to 'random_chars.txt'.

'random_chars.txt' is then used to create an image consisting of random text
which we will run Tesseract's OCR on.
"""

from random import randint
import os


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


def rand_chars(n):
    """Return a string consisting of n random chars."""
    rv = ""
    for i in range(n):
        rv += chr(randint(33, 126))
    return rv


def write_to_file(text, file_name="random_chars.txt"):
    """Write a given string to a text file."""
    f = open(get_absolute_path(file_name), 'w')
    f.write(text)
    f.flush()
    f.close()


def main():
    """Generate n random characters, and write these to 'random_chars.txt'."""
    n = 5000
    write_to_file(rand_chars(n))


if __name__ == "__main__":
    main()
