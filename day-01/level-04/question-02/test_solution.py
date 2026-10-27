import unittest
from typing import List
from collections import defaultdict

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    """Solution function copied for testing."""
    if k == 0:
        return 0
    left = 0
    max_len = 0
    count = defaultdict(int)
    distinct = 0
    for right, num in enumerate(nums):
        if count[num] == 0:
            distinct += 1
        count[num] += 1
        while distinct > k:
            left_num = nums[left]
            count[left_num] -= 1
            if count[left_num] == 0:
                distinct -= 1
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len

class TestLongestSubarrayAtMostKDistinct(unittest.TestCase):
    def test_example1(self):
        nums = [1,2,1,2,3]
        k = 2
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 4)

    def test_example2(self):
        nums = [1,2,3,4,5]
        k = 1
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 1)

    def test_example3(self):
        nums = [1,1,1,1,1]
        k = 2
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 5)

    def test_single_element(self):
        nums = [5]
        k = 1
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 1)

    def test_k_equals_length(self):
        nums = [1,2,3,4]
        k = 4
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 4)

    def test_all_same_large_k(self):
        nums = [7,7,7,7]
        k = 10
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 4)

    def test_negative_numbers(self):
        nums = [-1,-2,-1,-2,-3]
        k = 2
        self.assertEqual(longest_subarray_at_most_k_distinct(nums, k), 4)

if __name__ == '__main__':
    unittest.main()
