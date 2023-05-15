from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    def test_place(self):
        self.assertEqual("", Place().name)
