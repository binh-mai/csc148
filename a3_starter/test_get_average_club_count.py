"""A3. Test cases for function get_average_club_count from club_functions
"""

from club_functions import get_average_club_count


def test_empty() -> None:
    """Test get_average_club_count with empty dict"""

    assert get_average_club_count({}) == 0


def test_one_person_one_club() -> None:
    """Test get_average_club_count with one person who is in one club."""

    param = {'Claire Dunphy': ['Parent Teacher Association']}
    actual = get_average_club_count(param)
    expected = 1

    assert actual == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['test_get_average_club_count.py'])
