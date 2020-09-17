# What's the good of that?
[![PyPI version](https://badge.fury.io/py/try-parse.svg)](https://pypi.org/project/try-parse/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/try-parse)](https://img.shields.io/pypi/pyversions/try-parse)
[![License](https://img.shields.io/pypi/l/try-parse)](https://img.shields.io/pypi/l/try-parse)
1. Cast the string representation of simple objects to the desired type.
1. Safe type casting. The exception will not be thrown. The function returns status and result.
## install
```
pip install try-parse
```
## import
``` python
from try_parse.utils import ParseUtils
```
## try_parse_date
Parse object to date
``` python
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
```
## try_parse_datetime
Parse object to datetime
``` python
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
```
## try_parse_int
Parse object to int
``` python
status, target = ParseUtils.try_parse_int('19')
self.assertTrue(status)
self.assertIsInstance(target, int)
self.assertEqual(target, 19)

status, target = ParseUtils.try_parse_int('Invalid')
self.assertFalse(status)
self.assertIsNone(target)
```
## try_parse_float
Parse object to float
``` python
status, target = ParseUtils.try_parse_float('19.00')
self.assertTrue(status)
self.assertIsInstance(target, float)
self.assertEqual(target, 19.00)

status, target = ParseUtils.try_parse_float('Invalid')
self.assertFalse(status)
self.assertIsNone(target)
```
## try_parse_decimal
Parse object to decimal
``` python
status, target = ParseUtils.try_parse_decimal('19.00')
self.assertTrue(status)
self.assertIsInstance(target, Decimal)
self.assertEqual(target, Decimal(19))

status, target = ParseUtils.try_parse_decimal('Invalid')
self.assertFalse(status)
self.assertIsNone(target)
```
## try_parse_bool
Parse object to bool
``` python
for p in ["yes", "true", "t", "1", 1]:
    status, target = ParseUtils.try_parse_bool(p)
    self.assertTrue(status)
    self.assertIsInstance(target, bool)
    self.assertTrue(target)

status, target = ParseUtils.try_parse_bool('Invalid')
self.assertFalse(status)
self.assertIsNone(target)
```
