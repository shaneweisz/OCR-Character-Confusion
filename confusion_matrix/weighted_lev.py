from file_comparison import get_relative_path
import numpy as np
import pandas as pd
import weighted_levenshtein as wl
import sys


def normalise(df):
    """
    Returns a normalised Confusion Matrix.

    Each count in a row is converted to the proportion of times that
    character i is read as character j.
    """
    v = np.sum(df, axis=1)       # a vector with the sum of each of the rows
    v = v.values.reshape(-1, 1)  # transpose v to be used to divide below
    df = np.divide(df, v)
    return df


def get_subsitution_costs(df):
    df = 1-df
    sub_costs = np.ones((128, 128), dtype=np.float64)  # make a 2D array of 1's
    for row in df.index.values:
        for col in df.columns.values:
            sub_costs[ord(row), ord(col)] = df.loc[row, col]
    return sub_costs


def main():
    df = pd.read_pickle(get_relative_path('../confusion_matrix') +
                        '/confusion_matrix.pkl')
    df = df.drop('other', axis=1)  # drop the ' ' column
    df = normalise(df)

    substitution_costs = get_subsitution_costs(df)
    # get the distance of truth from read:

    truth = sys.argv[1]
    read = sys.argv[2]
    print(wl.lev(read, truth, substitute_costs=substitution_costs))


if __name__ == "__main__":
    main()
