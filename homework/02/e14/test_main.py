import unittest

from main import calculate_sum, get_max, is_palindrome, reverse

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)

    def test_get_max(self):
        self.assertEqual(get_max(1, 2, 3), 3)
        self.assertEqual(get_max(-1, -2, -3), -1)
        self.assertEqual(get_max(0, 0, 0), 0)
        self.assertEqual(get_max(1, 1, 2), 2)
        self.assertEqual(get_max(5, 2, 3), 5)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("jani"), "inaj")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")