"""A simple checker for types of functions in club_functions.py"""

import pytest
import checker_generic
import io
import club_functions as cf

FILENAME = 'club_functions.py'
PYTA_CONFIG = 'a3_pythonta.json'
TARGET_LEN = 79
SEP = '='

EXAMPLE_PROFILE_DATA = '''Katsopolis, Jesse
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

CONSTANTS = {
    'EXAMPLE_PROFILE_DATA': EXAMPLE_PROFILE_DATA,
    'P2F': {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                                 'Rebecca Donaldson-Katsopolis'],
            'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
            'Stephanie J Tanner': ['Kimmy Gibbler', 'Michelle Tanner'],
            'Danny R Tanner': ['DJ Tanner-Fuller', 'Jesse Katsopolis',
                               'Joey Gladstone']},
    'P2C': {'Michelle Tanner': ['Comet Club'],
            'Danny R Tanner': ['Parent Council'],
            'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
            'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
            'Joey Gladstone': ['Comics R Us', 'Parent Council']}
}


class TestChecker:
    """Sanity checker for assignment functions."""

    def _set_up(self):
        self.sample_file = io.StringIO('''Pritchett, Jay
Pritchett, Gloria
Delgado, Manny
Dunphy, Claire

Dunphy, Claire
Parent Teacher Association
Dunphy, Phil
Pritchett, Mitchell
Pritchett, Jay
''')
        self.p2f = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                                         'Rebecca Donaldson-Katsopolis'],
                    'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
                    'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
                    'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                                       'Joey Gladstone']}

        self.p2c = {'Michelle Tanner': ['Comet Club'],
                    'Danny R Tanner': ['Parent Council'],
                    'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
                    'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
                    'Joey Gladstone': ['Comics R Us', 'Parent Council']}

    def test_00_load_profiles(self):
        """Function load_profiles."""
        self._set_up()

        print('\nChecking load_profiles...')

        result = cf.load_profiles(self.sample_file)
        error_message = checker_generic.type_error_message(
            'load_profiles',
            'tuple[dict[str, list[str]], dict[str, list[str]]]', type(result))

        assert isinstance(result, tuple), error_message
        assert len(result) == 2, \
            "load_profiles should return a 2-item tuple"

        self._is_dict_of_Ks_and_list_Vs(result[0], str, str,
                                        'load_profiles returns a 2-item tuple, but the first item '
                                        'should be of type dict[str, list[str]]')

        self._is_dict_of_Ks_and_list_Vs(result[1], str, str,
                                        'load_profiles returns a 2-item tuple, but the second item '
                                        'should be of type dict[str, list[str]]')

        print('  check complete')

    def test_01_get_average_club_count(self):
        """Function get_average_club_count."""
        self._set_up()

        self._check_simple_type(
            cf.get_average_club_count,
            [{'Jen Campbell': ['CS Profs']}],
            int)

    def test_02_get_last_to_first(self):
        """Function get_last_to_first."""
        self._set_up()

        print('\nChecking get_last_to_first...')

        result = cf.get_last_to_first(self.p2f)
        error_msg = 'get_last_to_first should return a dict[str, list[str]]'

        self._is_dict_of_Ks_and_list_Vs(result, str, str, error_msg)

        print('  check complete')

    def test_03_invert_and_sort(self):
        """Function invert_and_sort."""
        self._set_up()

        print('\nChecking invert_and_sort...')

        result = cf.invert_and_sort(self.p2c)
        error_message = checker_generic.type_error_message(
            'invert_and_sort', 'dict[object, list]', type(result))

        assert isinstance(result, dict), error_message
        for key in result:
            assert isinstance(result[key], list), \
                'invert_and_sort returns a dict, '
            'but one or more value(s) is not of type list'

        print('  check complete')

    def test_04_get_clubs_of_friends(self):
        """Function get_clubs_of_friends."""
        self._set_up()

        print('\nChecking get_clubs_of_friends...')

        self._check_list_of_Ts(
            cf.get_clubs_of_friends,
            [self.p2f, self.p2c, 'Stephanie J Tanner'],
            str)

        print('  check complete')

    def test_05_recommend_clubs(self):
        """Function recommend_clubs."""
        self._set_up()
        print('\nChecking recommend_clubs...')

        result = self._check_list_of_Ts(
            cf.recommend_clubs,
            [self.p2f, self.p2c, 'Jesse Katsopolis'],
            tuple)

        msg = 'recommend clubs should return list[tuple[str, int]'

        for item in result[1]:
            assert len(item) == 2, \
                msg + ', but one or more tuples does not contain 2 elements'

            assert isinstance(item[0], str), \
                msg + ', but the first item is not always of type str'

            assert isinstance(item[1], int), \
                msg + ', but the second item is not always of type int'

        print('  check complete')

    def _check_simple_type(self, func: callable, args: list, ret_type: type):
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.
        """

        print('\nChecking {}...'.format(func.__name__))
        result = checker_generic.type_check_simple(func, args, ret_type)
        assert result[0], result[1]

        print('  check complete')

    def _check_list_of_Ts(self, func: callable, args: list, ret_type: type):
        """Check that func called with arguments args returns a value of type
        ret_type.

        """

        result = checker_generic.returns_list_of_Ts(func, args, ret_type)
        assert result[0], result[1]
        return result

    def _is_dict_of_Ks_and_list_Vs(self, result: object, key_tp: type,
                                   val_tp: type, msg: str):
        """Check if result is a dict with keys of type key_tp and values
         of type list that are non-empty and with elements of type val_tp.

        """

        assert isinstance(result, dict), msg

        for (key, val) in result.items():
            assert isinstance(key, key_tp), (
                    msg + ', but one or more keys is not of type ' + str(key_tp))
            assert isinstance(val, list), (msg + ', but one or more values is not of type list')

            assert val != [], msg + ' and the values should be non-empty lists'
            for item in val:
                assert isinstance(item, val_tp), \
                    msg + ', but one or more items in the values list(s) is not of type ' + str(
                        val_tp)


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
pytest.main(['--show-capture', 'no', '--disable-warnings', '--tb=short',
             'a3_checker.py'])
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contract\n')
