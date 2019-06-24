import numpy as np
import pandas as pd


def matrix_from_data(truth_list, read_list, chars):
    '''
    Parameters:
    truth_list --> list of the true characters
    read_list  --> list of the corresponding recognized characters
    chars --> list of characters that are valid options for true characters

    Returns:
    A 2D Matrix A where A_ij represents the probability that
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
    totals = dict()
    for truth_char, read_char in zip(truth_list, read_list):
        totals[truth_char] = totals.get(truth_char, 0) + 1
        if read_char not in chars:
            df.loc[truth_char, 'other'] += 1
        else:
            df.loc[truth_char, read_char] += 1

    for char in chars:
        df.loc[char] /= totals.get(char, 1)
    return df


def main():
    truth_list = ['a', 'b', '0', '7', 'a', 'a', 'a']
    read_list = ['a', 'B', 'O', '?', 'a', 'a', 'b']
    chars = ['a', 'b', 'B', '0', 'O', '7']
    df = matrix_from_data(truth_list, read_list, chars)
    print(df)


if __name__ == "__main__":
    main()
