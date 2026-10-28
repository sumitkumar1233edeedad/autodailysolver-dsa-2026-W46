import unittest
from typing import List

def find_target_index(nums: List[int], target: int) -> int:
    """
    Returns the index of the first occurrence of target in nums.
    If target is not found, returns -1.
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

class TestFindTargetIndex(unittest.TestCase):
    def test_example1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(find_target_index(nums, target), 4)
    
    def test_example2(self):
        nums = [10, 20, 30, 40]
        target = 25
        self.assertEqual(find_target_index(nums, target), -1)
    
    def test_example3(self):
        nums = [5, 5, 5, 5]
        target = 5
        self.assertEqual(find_target_index(nums, target), 0)
    
    def test_target_at_beginning(self):
        nums = [1, 2, 3]
        target = 1
        self.assertEqual(find_target_index(nums, target), 0)
    
    def test_target_at_end(self):
        nums = [1, 2, 3]
        target = 3
        self.assertEqual(find_target_index(nums, target), 2)
    
    def test_single_element_found(self):
        nums = [42]
        target = 42
        self.assertEqual(find_target_index(nums, target), 0)
    
    def test_single_element_not_found(self):
        nums = [42]
        target = 0
        self.assertEqual(find_target_index(nums, target), -1)
    
    def test_negative_numbers(self):
        nums = [-5, -3, 0, 2, 4]
        target = -3
        self.assertEqual(find_target_index(nums, target), 1)
    
    def test_large_numbers(self):
        nums = [10**9, -10**9, 0]
        target = -10**9
        self.assertEqual(find_target_index(nums, target), 1)

if __name__ == '__main__':
    unittest.main()
