import decimal
from datetime import date, datetime
from decimal import Decimal
from typing import Tuple, Any, Optional


class ParseUtils:
    @staticmethod
    def try_parse_date(i: Any, format: str = None) -> Tuple[bool, Optional[date]]:
        """
        Parse object to date
        :param format: date format
        :param i: object
        :return: status, date object
        """
        if i is None:
            return True, i

        if type(i) == date:
            return True, i
        try:
            i = str(i)
            if format is None:
                return True, date.fromisoformat(i)
            else:
                return True, datetime.strptime(i, format).date()
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_datetime(i: Any, format: str = None) -> Tuple[bool, Optional[datetime]]:
        """
        Parse object to datetime
        :param format: datetime format
        :param i: object
        :return: status, datetime object
        """
        if i is None:
            return True, i

        if type(i) == datetime:
            return True, i
        try:
            i = str(i)
            if format is None:
                return True, datetime.fromisoformat(i)
            else:
                return True, datetime.strptime(i, format)
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_int(i: Any) -> Tuple[bool, Optional[int]]:
        """
        Parse object to int
        :param i: object
        :return: status, int object
        """
        if i is None:
            return True, i

        if type(i) == int:
            return True, i
        try:
            return True, int(i)
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_float(i: Any) -> Tuple[bool, Optional[float]]:
        """
        Parse object to float
        :param i: object
        :return: status, float object
        """
        if i is None:
            return True, i

        if type(i) == float:
            return True, i
        try:
            return True, float(i)
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_decimal(i: Any) -> Tuple[bool, Optional[Decimal]]:
        """
        Parse object to decimal
        :param i: object
        :return: status, decimal object
        """
        if i is None:
            return True, i

        if type(i) == Decimal:
            return True, i
        try:
            return True, Decimal(i)
        except (ValueError, decimal.InvalidOperation):
            return False, None

    @staticmethod
    def try_parse_bool(i: Any) -> Tuple[bool, Optional[bool]]:
        """
        Parse object to bool
        :param i: object
        :return: status, bool object
        """
        if i is None:
            return True, i

        if type(i) == bool:
            return True, i

        try:
            i = str(i).lower()

            if i not in ("yes", "true", "t", "1", "no", "false", "f", "0"):
                raise ValueError()

            return True, i in ("yes", "true", "t", "1", 1)
        except ValueError:
            return False, None
