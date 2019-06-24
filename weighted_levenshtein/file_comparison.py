import difflib
import os


def get_string(file_name):
    f = open(file_name,'r')
    str = f.read()
    str = "".join(str.split())
    return str


def get_relative_path(relative_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def main():
    str1 = get_string(get_relative_path("../char_data_generation/random_chars.txt"))
    str2 = get_string(get_relative_path("../char_data_generation/recognized_chars.txt"))
    print(str1[0:100])
    print(str2[0:100])


if __name__ == '__main__':
    main()
