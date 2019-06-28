import os
from needleman_wunsch import nw


def get_string(file_name):
    '''
    Parameters:
        file_name --> a string with a given file name

    Returns a string with all the content from a given file name
    '''
    f = open(file_name, 'r')
    string = f.read()
    f.close()
    return string


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


def align(truth, read):
    '''
    Parameters:
        truth --> a string with the true characters from the original file
        read --> a string with the corresponding ocr-ed characters

    Returns:
        A two-tuple with a string of the true characters and a string of
        the read characters that are aligned for comparison purposes.
    '''
    to_remove = ['\n', '\v', '\t', '\f']
    for rem in to_remove:
        truth, read = truth.replace(rem, ''), read.replace(rem, '')
    return nw(truth, read)


def main():  # Run in pypy3 for speed and store in a text file for later use
    truth = get_string(get_absolute_path(
        "../char_data_generation/random_chars.txt"))
    read = get_string(get_absolute_path(
        "../char_data_generation/recognized_chars.txt"))
    aligned_truth, aligned_read = align(truth, read)

    print(aligned_truth[-85:])  # For checking purposes
    print(aligned_read[-85:])
    # check whether / added at end of get_relative_path
    aligned_file = open(get_absolute_path('../confusion_matrix')+'/aligned_data.txt', 'w')
    aligned_file.write(aligned_truth + "\n" + aligned_read)
    aligned_file.close()


if __name__ == '__main__':
    main()
