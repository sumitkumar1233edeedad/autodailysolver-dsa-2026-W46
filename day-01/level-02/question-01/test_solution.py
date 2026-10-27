import unittest
from typing import List

# The function under test is assumed to be available in the same namespace
# (e.g., imported from the solution module).

class TestContainsDuplicate(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 1]
        self.assertTrue(containsDuplicate(nums))
    
    def test_example2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(containsDuplicate(nums))
    
    def test_example3(self):
        nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(containsDuplicate(nums))
    
    def test_single_element(self):
        nums = [5]
        self.assertFalse(containsDuplicate(nums))
    
    def test_all_same(self):
        nums = [2, 2, 2, 2]
        self.assertTrue(containsDuplicate(nums))
    
    def test_large_distinct(self):
        nums = list(range(10000))
        self.assertFalse(containsDuplicate(nums))
    
    def test_large_with_duplicate(self):
        nums = list(range(10000))
        nums.append(5000)
        self.assertTrue(containsDuplicate(nums))

if __name__ == '__main__':
    unittest.main()
