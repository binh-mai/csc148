"""CSC148 Prep 7: Recursion

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: David Liu and Diane Horton

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 David Liu and Diane Horton

=== Module description ===
This module contains sample tests for Prep 7.

Complete the TODO in this file.

When writing a test case, make sure you create a new function, with its
name starting with "test_". For example:

def test_my_test_case():
    # Your test here
"""
from prep7 import num_positives, nested_max, max_length

# Below are provided sample test cases for your use. You are encouraged
# to add additional test cases (in addition to the ones required above.)
# WARNING: THIS IS AN EXTREMELY INCOMPLETE SET OF TESTS!
# Add your own to practice writing tests and to be confident your code is
# correct.


def test_num_positives_doctest_example() -> None:
    """Test num_positive on one of the given doctest examples."""
    assert num_positives([1, -2, [-10, 2, [3], 4, -5], 4]) == 5


def test_num_positives_empty_list() -> None:
    """Test num_positive on an empty list."""
    assert num_positives([]) == 0


def test_num_positives_only_integers_list() -> None:
    """Test num_positive on a list with only integers (no sub-nested-list)."""
    assert num_positives([1, 33, 5, -24, 240, -8, 10, 99]) == 6


def test_num_positives_more_complicated_list() -> None:
    """Test num_positive on a more complicated list with
    multiple nested lists."""
    assert num_positives([1, -2, [-10, 2, [3, [-5, 7, [8]]], 4, -5], 4, []]) \
           == 7


def test_nested_max_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert nested_max([1, 2, [1, 2, [3], 4, 5], 4]) == 5


def test_nested_max_empty_list() -> None:
    """Test nested_max on an empty list."""
    assert nested_max([]) == 0


def test_nested_max_only_integers_list() -> None:
    """Test nested_max on a list with only integers (no sub-nested-list)."""
    assert nested_max([1, 33, 5, 24, 1206, 8, 10, 99]) == 1206


def test_nested_max_more_complicated_list() -> None:
    """Test nested_max on a more complicated list with
    multiple nested lists."""
    assert nested_max([6, 7, [1, 2, [3, [10, 9, [11]]], 4, 5], 4, []]) == 11


def test_max_length_doctest_example() -> None:
    """Test nested_max on one of the given doctest examples."""
    assert max_length([1, 2, [1, 2], 4]) == 4


def test_max_length_base_case() -> None:
    """Test nested_max on an integer (the base case)."""
    assert max_length(1) == 0


def test_max_length_empty_list() -> None:
    """Test nested_max on an empty list."""
    assert max_length([]) == 0


def test_max_length_only_integers_list() -> None:
    """Test nested_max on a list with only integers (no sub-nested-list)."""
    assert max_length([1, 33, 5, -24, 240, 8, 10, 99]) == 8


def test_max_length_more_complicated_list() -> None:
    """Test max_length on a more complicated list with
    multiple nested lists."""
    assert max_length([6, 7, [1, 2, [-3, [10, 9, [11, -4, 2, 19, 50, -58]]],
                              4, -5, [29, -5], [], 210], 4, []]) == 8


if __name__ == '__main__':
    import pytest
    pytest.main(['prep7_starter_tests.py'])
