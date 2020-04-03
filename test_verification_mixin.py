import unittest 
from verification_mixin import VerificationMixin


class TestClassVerificationMixin(unittest.TestCase):

    def test_if_verify_value_returns_error_if_given_negative_value(self):
        v = VerificationMixin()
        err = None

        try:
            v.verify_number_value(-1)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err),"Value should not be negative")

    def test_if_verify_health_returs_error_if_given_negative_health(self):
        v = VerificationMixin()
        err = None

        try:
            v.verify_health(0)
        except Exception as exc:
            err = exc

        self.assertIsNotNone(err)
        self.assertEqual(str(err),"Health should be above 0")

    def test_if_verify_if_more_than_max_returns_value_when_value_is_less_than_max(self):
        v = VerificationMixin()

        res = v.verify_if_more_than_max(value = 10, max_value = 20)
        exp = 10

        self.assertEqual(res,exp)

    def test_if_verify_if_more_than_max_returns_max_value_if_value_is_more_than_max(self):
        v = VerificationMixin()

        res = v.verify_if_more_than_max(value = 500, max_value = 20)
        exp = 20

        self.assertEqual(res,exp)


if __name__ == '__main__':
    unittest.main()