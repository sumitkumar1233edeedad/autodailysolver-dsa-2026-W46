import unittest
from typing import List

class TestPartitionBySign(unittest.TestCase):
    def assertPartitioned(self, original: List[int], result: List[int]) -> None:
        # Check same elements
        self.assertEqual(sorted(original), sorted(result))
        # Check partition property
        seen_non_negative = False
        for x in result:
            if x < 0:
                if seen_non_negative:
                    self.fail(f"Array not partitioned correctly: {result}")
            else:
                seen_non_negative = True

    def test_example1(self):
        nums = [3, -1, -2, 4, 0, -5]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_example2(self):
        nums = [-1, 2, -3, 4]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_example3(self):
        nums = [1, 2, 3]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_all_negatives(self):
        nums = [-5, -1, -3]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_all_positives(self):
        nums = [5, 1, 3]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_single_negative(self):
        nums = [-10]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_single_positive(self):
        nums = [10]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_zeros(self):
        nums = [0, -1, 0, -2, 0]
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

    def test_empty(self):
        nums = []
        original = nums.copy()
        result = partition_by_sign(nums)
        self.assertPartitioned(original, result)

if __name__ == "__main__":
    unittest.main()
