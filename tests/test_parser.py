import unittest

from parser import UserParser


class TestUserParser(unittest.TestCase):

    def test_complete_data(self):
        data = {
            "id": 1,
            "username": "Alice",
            "email": "alice@example.com",
            "address": {
                "city": "London",
                "zipcode": "12345"
            }
        }

        user = UserParser.from_dict(data)

        self.assertEqual(user.username, "Alice")
        self.assertEqual(user.city, "London")
        self.assertEqual(user.zipcode, "12345")

    def test_missing_address(self):
        data = {
            "id": 2,
            "username": "Bob",
            "email": "bob@test.com"
        }

        user = UserParser.from_dict(data)

        self.assertEqual(user.city, "Unknown")
        self.assertEqual(user.zipcode, "Unknown")

    def test_missing_username(self):
        data = {
            "id": 3,
            "email": "test@test.com"
        }

        user = UserParser.from_dict(data)

        self.assertEqual(user.username, "Anonymous")

    def test_missing_id(self):
        data = {
            "username": "Alice"
        }

        with self.assertRaises(KeyError):
            UserParser.from_dict(data)


if __name__ == "__main__":
    unittest.main()
