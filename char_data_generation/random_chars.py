from random import randint
import os


def get_absolute_path(relative_path):
    '''
    Parameters:
        relative_path --> a string with the path to a file relative to the
                          current directory
                          Example: "../char_data_generation/random_chars.txt"

    Returns:
        A string with the absolute file path to a given file
    '''
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def rand_chars(n):
    """
    Returns a string consisting of n random chars
    """
    rv = ""
    for i in range(n):
        rv += chr(randint(33, 126))
    return rv


def write_to_file(text, file_name="random_chars.txt"):
    f = open(get_absolute_path(file_name), 'w')
    f.write(text)
    f.flush()
    f.close()


def main():
    n = 5000
    write_to_file(rand_chars(n))


if __name__ == "__main__":
    main()
