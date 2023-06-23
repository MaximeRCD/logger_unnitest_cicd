import unittest
import datetime
from modules.utility.date import getTodayString


class TestDateModule(unittest.TestCase):

    def test_getTodayStringNoTz(self):
        self.assertEqual(getTodayString(), datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M"))


TestDateModule.test_getTodayStringNoTz()
