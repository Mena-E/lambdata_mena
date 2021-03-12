"""
Basic Unit Tests for lambdata_mena2 Package

"""

import pandas as pd
from lambdata_mena2.helper_function import CleanFrame
from lambdata_mena2.helper_function import RandomSplit
from lambdata_mena2.helper_function import TimeSeriesSplit

# Importing csv files to test helper functions
df_oil = pd.read_csv("oil_consumption_per_cap.csv")
df_sp = pd.read_csv("^GSPC.csv")

# Instantiating classes
clean_df = CleanFrame(df_oil)
random_df = RandomSplit(df_oil, 0.8)
time_df = TimeSeriesSplit(df_sp, 0.8)


def test_my_clean_frame():
    """
    Testing that the null_count function works properly
    """
    assert isinstance(df_oil, pd.DataFrame)  # True
    assert clean_df.null_count() == 281  # 281


def test_random_split():
    """
    Testing random data splits with train_test_split function
    """
    assert len(df_oil) == 77
    assert len(random_df.train_test_split()[0]) == 62
    assert len(random_df.train_test_split()[1]) == 15


def test_time_series_split():
    """
    Testing time series data split with train_test_split function
    """
    assert len(df_sp) == 208
    assert len(time_df.train_test_split()[0]) == 166
    assert len(time_df.train_test_split()[1]) == 41
    assert time_df.train_test_split()[0].iloc[0, 0] < \
        time_df.train_test_split()[1].iloc[0, 0]
