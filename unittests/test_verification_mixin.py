import unittest
import sys

sys.path.append('..')

from helpers_and_utilities.verification_mixin import VerificationMixin


class TestClassVerificationMixin(unittest.TestCase):

    def test_if_verify_string_value_raiser_error(self):
        v = VerificationMixin()
        err = None

        try:
            v.verify_string_value('')
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), 'Value cannot be an empty string')

    def test_if_verify_number_value_returns_error_if_given_negative_value(self):
        v = VerificationMixin()
        err = None

        try:
            v.verify_number_value(-1)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "Value should not be negative")

    def test_if_verify_health_returs_error_if_given_negative_or_zero_health(self):
        v = VerificationMixin()
        err = None

        try:
            v.verify_health(0)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "Health should be above 0")

    def test_if_verify_if_more_than_max_returns_value_when_value_is_less_than_max(self):
        v = VerificationMixin()

        res = v.verify_if_more_than_max(value=10, max_value=20)
        exp = 10

        self.assertEqual(res, exp)

    def test_if_verify_if_more_than_max_returns_max_value_if_value_is_more_than_max(self):
        v = VerificationMixin()

        res = v.verify_if_more_than_max(value=500, max_value=20)
        exp = 20

        self.assertEqual(res, exp)

    def test_if_verify_command_raises_error_if_given_key_in_a_dictionary_is_not_there(self):
        dicts = {'one': 1, 'two': 2}
        key = 'three'
        err = None

        try:
            VerificationMixin.verify_command(dicts, key)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err), "No such command. Try again")


if __name__ == '__main__':
    unittest.main()
