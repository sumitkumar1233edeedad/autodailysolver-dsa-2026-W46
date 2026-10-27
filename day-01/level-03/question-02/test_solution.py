import unittest

class TestMoveZeroes(unittest.TestCase):
    def test_example1(self):
        nums = [0, 1, 0, 3, 12]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example2(self):
        nums = [0]
        moveZeroes(nums)
        self.assertEqual(nums, [0])

    def test_example3(self):
        nums = [1, 2, 3]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_all_zeros(self):
        nums = [0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_no_zeros(self):
        nums = [4, 5, 6]
        moveZeroes(nums)
        self.assertEqual(nums, [4, 5, 6])

    def test_single_non_zero(self):
        nums = [7]
        moveZeroes(nums)
        self.assertEqual(nums, [7])

    def test_mixed_negative(self):
        nums = [0, -1, 0, -3, 12]
        moveZeroes(nums)
        self.assertEqual(nums, [-1, -3, 12, 0, 0])

if __name__ == '__main__':
    unittest.main()
