import unittest
from datetime import datetime, timedelta
from dates.functions import today, substract_days


class MyModuleTests(unittest.TestCase):
    def test_today(self):
        # Test if the returned value is a string
        self.assertIsInstance(today(), str)

        # Test if the returned value has the correct format
        self.assertRegex(today(), r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")

    def test_subtract_days(self):
        # Test subtracting 1 day
        date_str = "2023-06-01 10:30"
        result = substract_days(date_str, 1)
        expected = "2023-05-31 10:30"
        self.assertEqual(result, expected)

        # Test subtracting 7 days
        date_str = "2023-06-10 08:00"
        result = substract_days(date_str, 7)
        expected = "2023-06-03 08:00"
        self.assertEqual(result, expected)

        # Test subtracting 30 days
        date_str = "2023-03-15 18:45"
        result = substract_days(date_str, 30)
        expected = "2023-02-13 18:45"
        self.assertEqual(result, expected)

        # Test subtracting 0 days (should return the same date)
        date_str = "2023-12-31 23:59"
        result = substract_days(date_str, 0)
        expected = "2023-12-31 23:59"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
