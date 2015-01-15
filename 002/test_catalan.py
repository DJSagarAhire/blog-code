import unittest
from catalan import *

class TestRecursive(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(catalan_recursive(0), 1)

    def test_one(self):
        self.assertEqual(catalan_recursive(1), 1)

    def test_six(self):
        self.assertEqual(catalan_recursive(6), 132)

class TestIterative(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(catalan_iterative(0), 1)

    def test_one(self):
        self.assertEqual(catalan_iterative(1), 1)

    def test_six(self):
        self.assertEqual(catalan_iterative(6), 132)

class TestProduct(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(catalan_product(0), 1)

    def test_one(self):
        self.assertEqual(catalan_product(1), 1)

    def test_five(self):
        self.assertEqual(catalan_product(5), 42)

    def test_six(self):
        self.assertEqual(catalan_product(6), 132)
