import unittest

from models.user import User


class TestUser(unittest.TestCase):
    def test_user_email(self):
        user = User()
        user.email = "someemail.com"
        self.assertEqual(0, len(User.email))

    def test_user_password(self):
        self.assertEqual("", User.password)

    def test_user_first_name(self):
        user = User()
        user.first_name = "victor"
        self.assertEqual("", User.first_name)

    def test_user_last_name(self):
        user = User()
        user.last_name = "Dubonus"
        self.assertEqual("", User.last_name)
