import unittest

from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        # Test the function with valid name
        self.assertTrue(is_name("Ville Virtanen"))
        self.assertTrue(is_name("Tiina Virtanen"))

        # Test the function with invalid name
        self.assertFalse(is_name("ville"))
        self.assertFalse(is_name("Tiina"))
        self.assertFalse(is_name("Tiina Virtanen0123"))
        self.assertFalse(is_name("1Tiina Virtanen"))
        self.assertFalse(is_name("Tiina Virtanen "))
        self.assertFalse(is_name(" Tiina Virtanen"))

if __name__ == '__main__':
    unittest.main()
