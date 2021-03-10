""" lambdata_mena2 - A collection of Data Science helper functions"""

import pandas
import numpy

def null_count(df):
    """Checks a dataframe for nulls and returns
       the number of missing values.
    """
    return df.isna().sum().sum()

def train_test_split(df, frac):
    """ Splits a dataframe into a training and testing
        and a testing set based on frac (a fraction) of
        the percent of the size of the training data, and
        returns the training
    """
    val = int(round(len(df) * frac, 0))
    df_train = df.iloc[0:val, :]
    df_test = df.iloc[val + 1:, :]
    print(df_train)
    print(df_test)
