import unittest
from typing import List

# The solution function is assumed to be available in the same namespace.
# If running standalone, uncomment the following implementation:
# def max_prefix_suffix_sum(nums: List[int]) -> int:
#     total = sum(nums)
#     prefix = 0
#     max_prefix = 0
#     ans = 0
#     n = len(nums)
#     for j in range(n + 1):
#         candidate = max_prefix + total - prefix
#         if candidate > ans:
#             ans = candidate
#         if j < n:
#             prefix += nums[j]
#             if prefix > max_prefix:
#                 max_prefix = prefix
#     return ans

class TestMaxPrefixSuffixSum(unittest.TestCase):
    def test_example1(self):
        nums = [1, -2, 3, -4, 5]
        self.assertEqual(max_prefix_suffix_sum(nums), 7)
    
    def test_example2(self):
        nums = [-1, -2, -3]
        self.assertEqual(max_prefix_suffix_sum(nums), 0)
    
    def test_example3(self):
        nums = [2, 3, -1, 4, -2, 5]
        self.assertEqual(max_prefix_suffix_sum(nums), 13)
    
    def test_all_positive(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(max_prefix_suffix_sum(nums), 10)
    
    def test_all_negative(self):
        nums = [-5, -2, -10]
        self.assertEqual(max_prefix_suffix_sum(nums), 0)
    
    def test_single_element_positive(self):
        nums = [5]
        self.assertEqual(max_prefix_suffix_sum(nums), 5)
    
    def test_single_element_negative(self):
        nums = [-5]
        self.assertEqual(max_prefix_suffix_sum(nums), 0)
    
    def test_mixed_with_zero(self):
        nums = [0, -1, 2, -3, 4]
        self.assertEqual(max_prefix_suffix_sum(nums), 5)
    
    def test_large_input(self):
        nums = [1, -1] * 50000  # length 100000
        self.assertEqual(max_prefix_suffix_sum(nums), 1)

if __name__ == "__main__":
    unittest.main()
