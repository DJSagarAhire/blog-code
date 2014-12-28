import unittest
from fibonacci import *

class TestRecursive(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fifteen(self):
        self.assertEqual(fibonacci_recursive(15), 610)

class TestIterative(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci_iterative(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci_iterative(1), 1)

    def test_fifteen(self):
        self.assertEqual(fibonacci_iterative(15), 610)

class TestEfficient(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibonacci_efficient(0), 0)

    def test_one(self):
        self.assertEqual(fibonacci_efficient(1), 1)

    def test_fifteen(self):
        self.assertEqual(fibonacci_efficient(15), 610)
