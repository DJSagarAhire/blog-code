import unittest
from levenshtein import *

class TestRecursive(unittest.TestCase):

    def test_same_strings(self):
        self.assertEqual(levenshtein_recursive('tars', 'tars'), 0)

    def test_empty_first_string(self):
        self.assertEqual(levenshtein_recursive('', 'tars'), 4)

    def test_empty_second_string(self):
        self.assertEqual(levenshtein_recursive('tars', ''), 4)

    def test_same_length(self):
        self.assertEqual(levenshtein_recursive('tars', 'cart'), 2)

    def test_different_length(self):
        self.assertEqual(levenshtein_recursive('tars', 'aries'), 3)

class TestDP(unittest.TestCase):

    def test_same_strings(self):
        self.assertEqual(levenshtein_dp('tars', 'tars'), 0)

    def test_empty_first_string(self):
        self.assertEqual(levenshtein_dp('', 'tars'), 4)

    def test_empty_second_string(self):
        self.assertEqual(levenshtein_dp('tars', ''), 4)

    def test_same_length(self):
        self.assertEqual(levenshtein_dp('tars', 'cart'), 2)

    def test_different_length(self):
        self.assertEqual(levenshtein_dp('tars', 'aries'), 3)

    def test_large_strings(self):
        self.assertEqual(levenshtein_dp('interstellar', 'interstate'), 5)
