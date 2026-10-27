import unittest

class TestFirstUniqueElement(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(first_unique_element([2, 3, 4, 2, 3, 5]), 4)
    def test_example2(self):
        self.assertEqual(first_unique_element([1, 1, 2, 2, 3, 3]), -1)
    def test_example3(self):
        self.assertEqual(first_unique_element([5]), 5)
    def test_all_unique(self):
        self.assertEqual(first_unique_element([1, 2, 3]), 1)
    def test_first_unique_then_duplicates(self):
        self.assertEqual(first_unique_element([1, 2, 2, 3, 3]), 1)
    def test_negative_numbers(self):
        self.assertEqual(first_unique_element([-1, -2, -1]), -2)
    def test_empty_list(self):
        self.assertEqual(first_unique_element([]), -1)

if __name__ == '__main__':
    unittest.main()
