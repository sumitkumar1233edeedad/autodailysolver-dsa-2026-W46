import unittest
from typing import List
from collections import Counter


def partition_by_frequency(nums: List[int], k: int) -> List[int]:
    """
    Partitions nums in-place so that elements with frequency > k come first.
    Returns the modified nums.
    """
    if not nums:
        return nums
    
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        if freq[nums[left]] > k:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    
    return nums


class TestPartitionByFrequency(unittest.TestCase):
    def _verify_partition(self, original: List[int], k: int, result: List[int]) -> None:
        """Verify that result is the same object as original and correctly partitioned."""
        self.assertIs(result, original, "Function must return the same list object (in-place modification)")
        
        # Compute frequencies from original
        freq = Counter(original)
        
        # Find partition point: first index where freq <= k
        partition_idx = 0
        while partition_idx < len(result) and freq[result[partition_idx]] > k:
            partition_idx += 1
        
        # All elements before partition_idx must have freq > k
        for i in range(partition_idx):
            self.assertGreater(freq[result[i]], k, f"Element {result[i]} at index {i} should have freq > {k}")
        
        # All elements from partition_idx onward must have freq <= k
        for i in range(partition_idx, len(result)):
            self.assertLessEqual(freq[result[i]], k, f"Element {result[i]} at index {i} should have freq <= {k}")
        
        # Ensure multiset is preserved
        self.assertEqual(Counter(result), freq)
    
    def test_example1(self):
        original = [1, 2, 3, 1, 2, 4]
        k = 1
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_example2(self):
        original = [5, 5, 5, 5]
        k = 2
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_example3(self):
        original = [10, 20, 30]
        k = 0
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_all_low_frequency(self):
        original = [1, 2, 3]
        k = 1
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_single_element(self):
        original = [7]
        k = 0
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_negative_numbers(self):
        original = [-1, -1, 2, 3]
        k = 1
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_mixed_frequencies(self):
        original = [4, 4, 4, 5, 5, 6, 7, 7, 7, 7]
        k = 2
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_k_larger_than_max_freq(self):
        original = [1, 2, 2, 3, 3, 3]
        k = 5
        result = partition_by_frequency(original, k)
        self._verify_partition(original, k, result)
    
    def test_empty_list(self):
        original = []
        k = 0
        result = partition_by_frequency(original, k)
        self.assertIs(result, original)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
