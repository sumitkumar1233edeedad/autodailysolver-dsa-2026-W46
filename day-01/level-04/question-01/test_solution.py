import unittest
from typing import List

# The function minSubArrayLen is expected to be available from the solution code.

class TestMinSubArrayLen(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(minSubArrayLen(7, [2,3,1,2,4,3]), 2)
    
    def test_example2(self):
        self.assertEqual(minSubArrayLen(4, [1,4,4]), 1)
    
    def test_example3(self):
        self.assertEqual(minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 0)
    
    def test_single_element_meets_target(self):
        self.assertEqual(minSubArrayLen(5, [5]), 1)
        self.assertEqual(minSubArrayLen(3, [10]), 1)
    
    def test_single_element_below_target(self):
        self.assertEqual(minSubArrayLen(10, [5]), 0)
    
    def test_whole_array_sum_equals_target(self):
        self.assertEqual(minSubArrayLen(15, [1,2,3,4,5]), 5)
    
    def test_multiple_subarrays_minimal(self):
        self.assertEqual(minSubArrayLen(6, [1,2,3,4,5]), 2)  # [2,4] sum=6 length=2
    
    def test_large_target_unreachable(self):
        self.assertEqual(minSubArrayLen(100, [1,2,3]), 0)
    
    def test_empty_array(self):
        # According to constraints, nums.length >= 1, but we test for robustness.
        self.assertEqual(minSubArrayLen(5, []), 0)

if __name__ == '__main__':
    unittest.main()