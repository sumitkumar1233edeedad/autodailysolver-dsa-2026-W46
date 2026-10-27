import unittest
from typing import List

# The function productExceptSelf is defined in the solution_code and will be available in the global namespace.

class TestProductExceptSelf(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_example3(self):
        nums = [2, 3, 4, 5]
        expected = [60, 40, 30, 24]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_two_elements(self):
        nums = [5, 10]
        expected = [10, 5]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = [0, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_negative_numbers(self):
        nums = [-2, -3, -4]
        expected = [12, 8, 6]
        self.assertEqual(productExceptSelf(nums), expected)

    def test_single_zero(self):
        nums = [0, 4, 5]
        expected = [20, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected)

if __name__ == '__main__':
    unittest.main()
