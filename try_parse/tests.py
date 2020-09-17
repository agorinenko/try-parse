import unittest
from datetime import date, datetime
from decimal import Decimal

from try_parse.utils import ParseUtils


class Tests(unittest.TestCase):
    def test_try_parse_date(self):
        status, target = ParseUtils.try_parse_date('2018-11-23')
        self.assertTrue(status)
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        # See format https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        status, target = ParseUtils.try_parse_date('23.11.2018', format='%d.%m.%Y')
        self.assertTrue(status)
        self.assertIsInstance(target, date)
        self.assertEqual(target, date(2018, 11, 23))

        status, target = ParseUtils.try_parse_date('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)

    def test_try_parse_datetime(self):
        status, target = ParseUtils.try_parse_datetime('2018-11-23 01:45:59')
        self.assertTrue(status)
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        # See format https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        status, target = ParseUtils.try_parse_datetime('23.11.2018T01:45:59', format='%d.%m.%YT%H:%M:%S')
        self.assertTrue(status)
        self.assertIsInstance(target, datetime)
        self.assertEqual(target, datetime(2018, 11, 23, 1, 45, 59))

        status, target = ParseUtils.try_parse_datetime('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)

    def test_try_parse_int(self):
        status, target = ParseUtils.try_parse_int('19')
        self.assertTrue(status)
        self.assertIsInstance(target, int)
        self.assertEqual(target, 19)

        status, target = ParseUtils.try_parse_int('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)

    def test_try_parse_float(self):
        status, target = ParseUtils.try_parse_float('19.00')
        self.assertTrue(status)
        self.assertIsInstance(target, float)
        self.assertEqual(target, 19.00)

        status, target = ParseUtils.try_parse_float('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)

    def test_try_parse_decimal(self):
        status, target = ParseUtils.try_parse_decimal('19.00')
        self.assertTrue(status)
        self.assertIsInstance(target, Decimal)
        self.assertEqual(target, Decimal(19))

        status, target = ParseUtils.try_parse_decimal('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)

    def test_try_parse_bool(self):
        for p in ["yes", "true", "t", "1", 1]:
            status, target = ParseUtils.try_parse_bool(p)
            self.assertTrue(status)
            self.assertIsInstance(target, bool)
            self.assertTrue(target)

        status, target = ParseUtils.try_parse_bool('Invalid')
        self.assertFalse(status)
        self.assertIsNone(target)
