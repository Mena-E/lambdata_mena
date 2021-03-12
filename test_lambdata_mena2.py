"""
Basic Unit Tests for lambdata_mena2 Package

"""

from random import randint
import pytest
import lambdata_mena2 as ld

# Testing __init__ in lambdata_mena2

#
# def test_increment_int():
#     """Making sure increment works for integers"""
#     x0 = 0
#     y0 = ld.increment(x0)  # 1
#     assert y0 == 1
#
#     x1 = 100
#     y1 = ld.increment(x1)  # 101
#     assert y1 == 101
#
#
# def test_increment_float():
#     """Making sure increment works for floats"""
#     x0 = 10.5
#     y0 = ld.increment(x0)  # 11.5
#     assert y0 == 11.5
#
#
# def test_increment_neg_int():
#     """Making sure increment works for negative integers"""
#     x0 = -1
#     y0 = ld.increment(x0)  # 0
#     assert y0 == 0
#
#
# def test_increment_neg_float():
#     """Making sure increment works for negative floats"""
#     x0 = -1.5
#     y0 = ld.increment(x0)  # -0.5
#     assert y0 == -0.5
#
#
# def test_colors():
#     """Testing that colors contain correct items"""
#     assert "Cyan" in ld.COLORS
#     assert "Mauve" in ld.COLORS
#     assert "Blue" in ld.COLORS
#     assert "Brown" not in ld.COLORS
#
#
# def test_number_colors():
#     """Testing number of elements in color"""
#     assert len(ld.COLORS) == 4  # 4


# Testing OOP_examples
user1 = ld.oop_example.SocialMediaUser(name="Nick", location="Arizona")
user2 = ld.oop_example.SocialMediaUser(name="Carl", location="Costa Rica", upvotes=250)


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