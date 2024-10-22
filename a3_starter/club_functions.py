""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import TextIO
import io

# Sample Data (Used by Docstring examples)
# What a Profile File might look like.
EXAMPLE_PROFILE_DATA =
'''
Katsopolis, Jesse
Parent Council
Rock N Rollers
Tanner, Danny R
Donaldson-Katsopolis, Rebecca
Gladstone, Joey

Donaldson-Katsopolis, Rebecca
Gibbler, Kimmy

Tanner, Stephanie J
Tanner, Michelle
Gibbler, Kimmy

Tanner, Danny R
Parent Council
Tanner-Fuller, DJ
Gladstone, Joey
Katsopolis, Jesse

Gibbler, Kimmy
Smash Club
Rock N Rollers

Gladstone, Joey
Comics R Us
Parent Council

Tanner, Michelle
Comet Club
'''

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
       'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

# Helper functions

EXAMPLE_PROFILE_DATA_2 = '''Fuentes, Diego
Gonzalez, Jorge
Wong, Samantha
Guerrero, Ana

Gonzalez, Jorge
Wong, Samantha
Fuentes, Diego

Wong, Samantha
Guerrero, Ana
Gonzalez, Jorge

Guerrero, Ana
Wong, Samantha

Lee, John
Lee, Mary
Park, Steve

Lee, Mary
Lee, John

Park, Steve
'''

P2F_2 = {'Diego Fuentes': ['Jorge Gonzalez'],
         'Jorge Gonzalez': ['Diego Fuentes', 'Samantha Wong'],
         'Samantha Wong': ['Ana Guerrero', 'Jorge Gonzalez'],
         'Ana Guerrero': ['Samantha Wong']}

P2C_2 = {'John Lee': [], 'Mary Lee': [], 'Steve Park': []}


def update_dict(key: str, value: str,
                key_to_values: dict[str, list[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def load_profiles(profiles_file: TextIO) -> tuple[dict[str, list[str]],
                                                  dict[str, list[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from
    profiles_file. The values in the two dictionaries are sorted in
    alphabetical order.

    >>> data = io.StringIO(EXAMPLE_PROFILE_DATA) # this treats a str as a file
    >>> result = load_profiles(data)
    >>> result == (P2F, P2C)
    True

    >>> data = io.StringIO(EXAMPLE_PROFILE_DATA_2)
    >>> result = load_profiles(data)
    >>> result == (P2F_2, P2C_2)
    True
    """
    person_to_friends = {}
    person_to_clubs = {}

    #first line and line after a blank line = '\n' -> key to person_to_friends
    # and person_to_clubs
    # line after that doesnt contain ',' -> clubs
    # line after that contain ',' -> friends

    line = profiles_file.readline().strip()



    # person_to_friends = {}
    # person_to_clubs = {}
    #
    # for line in profiles_file:
    #     line = line.strip()
    #     if not line or ',' not in line:
    #         continue
    #
    #     names = line.split(',')
    #     person = names[1].strip() + ' ' + names[0].strip()
    #     friends_or_clubs = names[2:]
    #
    #     for fc in friends_or_clubs:
    #         fc = fc.strip()
    #         if fc.isalpha():
    #             update_dict(person, fc, person_to_friends)
    #         else:
    #             update_dict(person, fc, person_to_clubs)
    #
    # for d in [person_to_friends, person_to_clubs]:
    #     for k in sorted(d.keys()):
    #         d[k].sort()
    #
    # return person_to_friends, person_to_clubs

#*********


def get_average_club_count(person_to_clubs: dict[str, list[str]]) -> int:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to, rounded down to the nearest integer (i.e. use // instead of /).

    >>> get_average_club_count(P2C)
    1

    >>> get_average_club_count(P2C_2)
    0
    """
    # TODO: add a second docstring example above
    # TODO: design and write the function body

    if not person_to_clubs:
        return 0

    total_club_count = sum(len(clubs) for clubs in person_to_clubs.values())
    person_count = len(person_to_clubs)
    average_club_count = total_club_count // person_count

    return average_club_count


def get_last_to_first(
        person_to_friends: dict[str, list[str]]) -> dict[str, list[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True

    >>> get_last_to_first(P2F_2) == {
    ...    'Fuentes': ['Diego'],
    ...    'Gonzalez': ['Jorge'],
    ...    'Wong': ['Samantha'],
    ...    'Guerrero': ['Ana']}
    True
    """
    # TODO: add a second docstring example above
    # TODO: design and write the function body

    last_to_first = {}
    people_list = []

    people_list.extend(person_to_friends.keys())
    values_list = person_to_friends.values()

    for value in values_list:
        people_list.extend(value)

    people_list.sort()

    for person in people_list:
        first_name = person.rsplit(' ', 1)[0]
        last_name = person.rsplit(' ', 1)[1]

        if last_name not in last_to_first:
            last_to_first[last_name] = [first_name]
        else:
            if first_name not in last_to_first[last_name]:
                last_to_first[last_name].append(first_name)

    return last_to_first

# ***************

def invert_and_sort(key_to_value: dict[object, object]) -> dict[object, list]:
    """Return key_to_value inverted so that each key in the returned dict
    is a value from the original dict (for non-list values) or each item from a
    value (for list values), and each value in the returned dict
    is a list of the corresponding keys from the original key_to_value.
    The value lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True

    >>> club_to_score = {'Parent Council': 3, 'Smash Club': 2, 'Orchestra': 2}
    >>> invert_and_sort(club_to_score) == {
    ...  3: ['Parent Council'], 2: ['Orchestra', 'Smash Club']}
    True

    >>> invert_and_sort(P2F_2) == {
    ...  'Jorge Gonzalez': ['Diego Fuentes', 'Samantha Wong'],
    ...  'Diego Fuentes': ['Jorge Gonzalez'],
    ...  'Samantha Wong': ['Ana Guerrero', 'Jorge Gonzalez'],
    ...  'Ana Guerrero': ['Samantha Wong']}
    True
    """
    # TODO: add a third docstring example above
    # TODO: design and write the function body

    inverted_dict = {}
    for key in key_to_value:
        if isinstance(key_to_value[key], list):
            for value in key_to_value[key]:
                update_dict(value, key, inverted_dict)
        else:
            if key_to_value[key] not in inverted_dict:
                inverted_dict[key_to_value[key]] = [key]
            else:
                inverted_dict[key_to_value[key]].append(key)

    for key in inverted_dict:
        inverted_dict[key].sort()

    return inverted_dict

#****************

def get_clubs_of_friends(person_to_friends: dict[str, list[str]],
                         person_to_clubs: dict[str, list[str]],
                         person: str) -> list[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']

    >>> get_clubs_of_friends(P2F, P2C, 'Kimmy Gibbler')
    ['Comics R Us', 'Parent Council', 'Rock N Rollers', 'Smash Club']
    """
    inverted_dict = invert_and_sort(person_to_friends)

    friends_1 = person_to_friends[person]
    friends_2 = inverted_dict[person]
    person_clubs = person_to_clubs[person]

    friends_clubs = []
    for friend in friends_1 and friends_2:
        if friend in person_to_clubs:
            friends_clubs.extend(person_to_clubs[friend])

    return sorted(set(friends_clubs) - set(person_clubs))



    # TODO: add a second docstring example above
    # TODO: design and write the function body
    # friends = person_to_friends.get(person, [])
    # clubs = []

    # for friend in friends:
    #     friend_clubs = person_to_clubs.get(friend, [])
    #     for club in friend_clubs:
    #         if club not in clubs and club not in person_to_clubs[person] and \
    #            all(club not in person_to_clubs[f] for f in person_to_friends[person] if f != friend):
    #             clubs.append(club)
    #
    # return sorted(clubs)


#helper function

def friends_in_club_score(person_to_friends: dict[str, list[str]],
                           person_to_clubs: dict[str, list[str]],
                           person: str,
                           club: str) -> int:
    """Return the score for the given club using the Friends in Club
    scoring system for the specified person.

    The score is the number of friends of the person who belong to the
    specified club.

    >>> friends_in_club_score(P2F, P2C, 'Jesse Katsopolis', 'Rock N Rollers')
    2
    """
    friends = person_to_friends.get(person, [])
    members = person_to_clubs.get(club, [])
    return len(set(friends).intersection(set(members)))


def different_club_score(person_to_friends: dict[str, list[str]],
                          person_to_clubs: dict[str, list[str]],
                          person: str,
                          club: str) -> int:
    """Return the score for the given club using the Different Club
    scoring system for the specified person.

    The score is the number of friends of the person who belong to a
    different club than the specified club.

    >>> different_club_score(P2F, P2C, 'Jesse Katsopolis', 'Rock N Rollers')
    1
    """
    friends = person_to_friends.get(person, [])
    other_clubs = set()
    for friend in friends:
        clubs = person_to_clubs.get(friend, [])
        other_clubs.update(clubs)
    other_clubs.discard(club)
    return len(other_clubs)


def recommend_clubs(
        person_to_friends: dict[str, list[str]],
        person_to_clubs: dict[str, list[str]],
        person: str) -> list[tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]

    >>> recommend_clubs
    """
    # TODO: add a second docstring example above
    # TODO: design and write the function body

    score1 = friends_in_club_score(person_to_friends, person_to_clubs, person)
    score2 = different_club_score(person_to_clubs, person)

    potential_score = {}
    clubs = invert_and_sort(person_to_clubs)
    for club in clubs:
        if club in score1:
            if club in score2:
                potential_score[club] = []
                potential_score[club] = score1[club]
        elif club in score2:
            if club not in potential_score:
                potential_score[club] = []
                potential_score[club] = score2[club]

    recommend_clubs_scores = list (potential_score.items())
    recommend_clubs_scores.sort()
    return recommend_clubs_scores


if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()
