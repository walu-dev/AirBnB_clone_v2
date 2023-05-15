from models.state import State
import unittest


class Test(unittest.TestCase):
    def test_state(self):
        self.assertEqual("", State().name)
