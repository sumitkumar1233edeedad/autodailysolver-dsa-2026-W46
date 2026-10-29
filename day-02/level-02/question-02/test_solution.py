import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 2, 4, 1]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [1, 2, 3, 4])

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        k = remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [0, 1, 2, 3, 4])

    def test_example3(self):
        nums = [5, 5, 5, 5]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [5])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        k = remove_duplicates(nums)
        self.assertEqual(k, 5)
        self.assertEqual(nums[:k], [1, 2, 3, 4, 5])

    def test_single_element(self):
        nums = [42]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [42])

    def test_all_same(self):
        nums = [7, 7, 7, 7, 7]
        k = remove_duplicates(nums)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [7])

    def test_negative_numbers(self):
        nums = [-1, -2, -1, 0, -2, 3]
        k = remove_duplicates(nums)
        self.assertEqual(k, 4)
        self.assertEqual(nums[:k], [-1, -2, 0, 3])

if __name__ == '__main__':
    unittest.main()
