import unittest

class TestSumOfUnique(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sum_of_unique([1, 2, 3, 2]), 4)
    
    def test_example2(self):
        self.assertEqual(sum_of_unique([1, 1, 1, 1, 1]), 0)
    
    def test_example3(self):
        self.assertEqual(sum_of_unique([1, 2, 3, 4, 5]), 15)
    
    def test_single_element(self):
        self.assertEqual(sum_of_unique([5]), 5)
    
    def test_all_duplicates(self):
        self.assertEqual(sum_of_unique([2, 2, 3, 3]), 0)
    
    def test_negative_numbers(self):
        self.assertEqual(sum_of_unique([-1, -2, -1, 3]), 1)  # -2 + 3 = 1

if __name__ == '__main__':
    unittest.main()