import pandas as pd
from file_comparison import get_string, get_absolute_path, align
import pickle
from collections import OrderedDict


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
    count_dict = OrderedDict()
    for char in chars:
        count_dict[char] = [0]*n
    count_dict['other'] = [0]*n  # for characters read in that are not in chars
    df = pd.DataFrame(count_dict, columns=count_dict.keys())
    df.index = chars
    for truth_char, read_char in zip(truth_list, read_list):
        if read_char not in chars:
            df.loc[truth_char, 'other'] += 1
        else:
            df.loc[truth_char, read_char] += 1

    df = df.drop(' ', axis=1)  # drop the ' ' column
    df = df.drop(' ')  # drop the ' ' row

    return df


def to_Hex(rgb_list):
    """
    Returns a hexadecimal string in the format '#RRGGBB'
    from a list decimal RGB values"
    """
    return "".join(map(lambda x: hex(x)[2:].rjust(2, "0"), rgb_list)).upper()


def visualise(df):
    '''
    Write a DataFrame to an excel file with conditional formatting
    '''
    writer = pd.ExcelWriter('confusion_matrix.xlsx', engine='xlsxwriter')
    df.to_excel(writer)
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.freeze_panes(1, 1)
    worksheet.conditional_format(1, 1, len(df.index), len(df.columns),
                                 {'type': '2_color_scale',
                                  'min_color': "#" + to_Hex([222, 238, 242]),
                                  'max_color': "#" + to_Hex([234, 50, 35])})
    writer.save()


def main():  # Read in aligned data from file (generated using pypy3 for speed)
    aligned_file = open(get_absolute_path('../confusion_matrix')
                        + '/aligned_data.txt', 'r')
    aligned_truth = aligned_file.readline()[:-1]  # trim to remove \n
    aligned_read = aligned_file.readline()
    aligned_file.close()

    chars = [chr(i) for i in range(32, 127)]  # 32 means include ' '
    df = matrix_from_data(aligned_truth, aligned_read, chars)

    try:  # try add to current pickle
        original_df = pd.read_pickle(get_absolute_path('../confusion_matrix') +
                                     '/confusion_matrix.pkl')
        df = df + original_df
    except FileNotFoundError:
        pass  # means pickle has not yet been created

    visualise(df)  # produce a formatted excel file for visualization

    df.to_pickle(get_absolute_path('../confusion_matrix') +
                 '/confusion_matrix.pkl')
    print(df.head())

    # df.loc['!'] --> returns the row of !
    # df['!'] --> returns the column of !


if __name__ == "__main__":
    main()
