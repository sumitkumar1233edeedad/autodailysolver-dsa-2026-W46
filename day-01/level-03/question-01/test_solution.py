import unittest
from typing import List

# Assuming the solution function is defined in the same module or imported.
# For the test, we'll define it again or import. Since we are providing both in JSON, we can just include the function in test_code? 
# The spec says test_code should be complete unittest.TestCase class testing the solution.
# We'll include the solution function inside test_code? But the solution_code is separate. In the test environment, they might run test_code after solution_code is defined. 
# To be safe, we can import the function from the solution module? But we don't have module name. 
# Usually in these tasks, the test_code is run in the same context as solution_code. So we can just use the function name.
# We'll write test_code assuming the function removeDuplicates is available.

class TestRemoveDuplicates(unittest.TestCase):
    def test_example1(self):
        nums = [1, 1, 2]
        k = removeDuplicates(nums)
        self.assertEqual(k, 2)
        self.assertEqual(nums[:k], [1, 2])
    
    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])
    
    def test_example3(self):
        nums = [1, 1, 1, 1]
        k = removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])
    
    def test_single_element(self):
        nums = [5]
        k = removeDuplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])
    
    def test_all_unique(self):
        nums = [-2, -1, 0, 1, 2]
        k = removeDuplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [-2, -1, 0, 1, 2])
    
    def test_empty_list(self):
        nums = []
        k = removeDuplicates(nums)
        self.assertEqual(k, 0)
        self.assertEqual(nums[:k], [])

if __name__ == '__main__':
    unittest.main()