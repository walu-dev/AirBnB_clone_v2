from models.city import City
import unittest


class Test(unittest.TestCase):
    def test_city(self):
        self.assertEqual("", City().name)