import nwalign as nw
import os


def get_string(file_name):
    f = open(file_name, 'r')
    string = f.read()
    f.close()
    return string


def get_relative_path(relative_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def main():
    truth = get_string(get_relative_path(
        "../char_data_generation/random_chars.txt"))
    print(truth)


if __name__ == "__main__":
    main()
