"""CSC148 Lab 1

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1

def test_first_item() -> None:
    """Test if the function correctly search for item at index 0"""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 0) == 0

def test_list_of_length_one() -> None:
    """Test if the function correctly search for item in a list with 1 item"""
    assert binary_search([0], 0) == 0

def test_not_in_list_of_length_one() -> None:
    """Test if the function correctly return -1 when item not in the list with
    length one"""
    assert binary_search([1], 0) == -1

def test_middle_item() -> None:
    """Test if the function correctly search for item in the middle
    of the list"""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 20) == 4

def test_last_item() -> None:
    """Test if the function correctly search for item in at the last
    of the list"""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 40) == 8

def test_near_middle_item() -> None:
    """Test if the function correctly search for item near the middle
    of the list"""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 15) == 3

def test_empty_list() -> None:
    """Test if the function correctly return -1 for an empty list"""
    assert binary_search([], 0) == -1

def test_second_half_of_list() -> None:
    """Test if the function correctly search for item in the second half
    of the list"""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 35) == 7

if __name__ == '__main__':
    import pytest
    pytest.main(['test_search.py'])
