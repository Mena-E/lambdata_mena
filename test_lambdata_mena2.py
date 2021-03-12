"""
Basic Unit Tests for lambdata_mena2 Package

"""

import pandas as pd
import pytest
from lambdata_mena2.oop_example import SocialMediaUser
from lambdata_mena2.helper_function import CleanFrame


# Testing OOP_examples
user1 = SocialMediaUser(name="Nick", location="Arizona")
user2 = SocialMediaUser(name="Carl", location="Costa Rica", upvotes=250)


def test_SMU_constructor():
    """Testing that SMU constructor works properly"""
    # testing name
    assert user1.name.lower() == "nick"
    assert user2.name.lower() == "carl"

    # testing location
    assert user1.location.lower() == "arizona"
    assert user2.location.lower() == "costa rica"

    # testing upvotes
    assert user1.upvotes == 0 # checks default
    assert user2.upvotes == 250


def test_unpopular():
    """Testing 0 upvotes is unpopular"""
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()


def test_popular():
    """Testing 250 is popular"""
    assert isinstance(user2.is_popular(), bool)
    assert user2.is_popular()


def test_SMU_constructor_types():
    """Testing types"""
    assert isinstance(user1.name, str)
    assert isinstance(user1.location, str)
    assert isinstance(user1.upvotes, int)


df = pd.read_csv("oil_consumption_per_cap.csv")
new_df = CleanFrame(df)

def test_my_clean_frame():
    assert isinstance(df, pd.DataFrame)
    assert new_df.null_count() == 281