"""A3. Test cases for function get_last_to_first from club_functions
"""

from club_functions import get_last_to_first


def test_empty() -> None:
    """Test get_last_to_first with empty dictionary."""

    assert get_last_to_first({}) == {}


def test_one_person_one_friend_same_last() -> None:
    """Test get_last_to_first with one person who has one friend that shares
    the same last name as them."""

    param = {'Clare Dunphy': ['Phil Dunphy']}
    actual = get_last_to_first(param)
    expected = {'Dunphy': ['Clare', 'Phil']}
    assert get_last_to_first(param) == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_last_to_first.py'])
