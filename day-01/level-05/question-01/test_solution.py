import unittest

class TestSubarraySum(unittest.TestCase):
    def test_example1(self):
        nums = [1, 1, 1]
        k = 2
        self.assertEqual(subarraySum(nums, k), 2)

    def test_example2(self):
        nums = [1, 2, 3]
        k = 3
        self.assertEqual(subarraySum(nums, k), 2)

    def test_example3(self):
        nums = [1, -1, 0]
        k = 0
        self.assertEqual(subarraySum(nums, k), 3)

    def test_single_element_match(self):
        nums = [5]
        k = 5
        self.assertEqual(subarraySum(nums, k), 1)

    def test_single_element_no_match(self):
        nums = [5]
        k = 3
        self.assertEqual(subarraySum(nums, k), 0)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        k = 0
        # Number of subarrays = n*(n+1)/2 = 3*4/2 = 6
        self.assertEqual(subarraySum(nums, k), 6)

    def test_negative_numbers(self):
        nums = [-1, -1, 1]
        k = -1
        # Subarrays: [-1] (index0), [-1] (index1), [-1,-1,1] (whole array) -> 3
        self.assertEqual(subarraySum(nums, k), 3)

    def test_large_k_no_subarray(self):
        nums = [1, 2, 3]
        k = 100
        self.assertEqual(subarraySum(nums, k), 0)

if __name__ == '__main__':
    unittest.main()