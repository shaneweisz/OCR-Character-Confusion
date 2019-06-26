import pandas as pd
from file_comparison import get_string, get_relative_path, align
import pickle


def matrix_from_data(truth_list, read_list, chars):
    '''
    Parameters:
    truth_list --> a string consisting of the true characters
    read_list  --> a string of the corresponding recognized characters
    chars --> list of characters that are valid options for true characters

    Returns:
    A 2D Matrix A where A_ij represents the number of times that
    character i is recognized as character j.

    '''
    assert len(truth_list) == len(read_list)
    n = len(chars)  # n is the number of valid true characters

    # Construct a Data Frame with truth values representing the rows
    # and recognized values as columns
    count_dict = dict()
    for char in chars:
        count_dict[char] = [0]*n
    count_dict['other'] = [0]*n  # for characters read in that are not in chars

    df = pd.DataFrame(count_dict)
    df.index = chars
    for truth_char, read_char in zip(truth_list, read_list):
        if read_char not in chars:
            df.loc[truth_char, 'other'] += 1
        else:
            df.loc[truth_char, read_char] += 1

    return df


def main():  # Read in aligned data from file (generated using pypy3 for speed)
    aligned_file = open('aligned_data.txt', 'r')
    aligned_truth = aligned_file.readline().strip()  # strip to remove \n
    aligned_read = aligned_file.readline()
    aligned_file.close()

    chars = [chr(i) for i in range(32, 127)]  # 32 means include ' '
    df = matrix_from_data(aligned_truth, aligned_read, chars)

    try:  # try add to current pickle
        original_df = pd.read_pickle(get_relative_path(
            'confusion_matrix_test.pkl'))
        df = df + original_df
    except FileNotFoundError:
        pass  # means pickle has not yet been created
    df.to_csv("confusion_matrix.csv")
    df.to_pickle("confusion_matrix_test.pkl")
    print(df.head())

    # df.loc['!'] --> returns the row of !
    # df['!'] --> returns the column of !


if __name__ == "__main__":
    main()
