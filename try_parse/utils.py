import decimal
from datetime import date, datetime
from decimal import Decimal


class ParseUtils:
    @staticmethod
    def try_parse_date(i) -> (bool, date):
        """
        Parse object to date
        :param i: object
        :return: status, date object
        """
        if i is None:
            return True, i

        if type(i) == date:
            return True, i
        try:
            return True, date.fromisoformat(str(i))
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_datetime(i) -> (bool, datetime):
        """
        Parse object to datetime
        :param i: object
        :return: status, datetime object
        """
        if i is None:
            return True, i

        if type(i) == datetime:
            return True, i
        try:
            return True, datetime.fromisoformat(str(i))
        except ValueError:
            return False, None

    @staticmethod
    def try_parse_int(i) -> (bool, int):
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
    def try_parse_float(i) -> (bool, float):
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
    def try_parse_decimal(i) -> (bool, Decimal):
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
    def try_parse_bool(i) -> (bool, bool):
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
