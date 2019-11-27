# try_parse project
Easily and safety cast objects to the desired data type
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
