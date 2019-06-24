import difflib
import os
import pytesseract


def get_string(file_name):
    f = open(file_name, 'r')
    string = f.read()
    string = string.split() # remove all whitespace
    #string = "".join(list(string)) # add a space between each character
    return string


def get_relative_path(relative_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path)
    return filename


def get_diff(str1, str2):
    d = difflib.Differ()
    return list(d.compare(str1, str2))


def main():
    truth = get_string(get_relative_path(
        "../char_data_generation/random_chars.txt"))
    read = get_string(get_relative_path(
        "../char_data_generation/recognized_chars.txt"))
    print(len(truth), truth[0:100])
    print(len(read), read[0:100])
    diff = get_diff(truth, read)
    for i in range(200):
        print(i, read[i],truth[i])
    #print('hi', diff)
    #for d in diff:
    #    print(d)


if __name__ == '__main__':
    main()
