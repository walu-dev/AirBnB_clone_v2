from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    def test_review(self):
        self.assertEqual("", Review().text)
