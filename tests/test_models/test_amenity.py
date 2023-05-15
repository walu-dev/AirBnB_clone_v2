from models.amenity import Amenity
import unittest


class Test(unittest.TestCase):
    def test_amenity(self):
        self.assertEqual("", Amenity().name)
