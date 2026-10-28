import unittest
from typing import List

# The spiralOrder function is expected to be defined in the solution_code.
# If running standalone, uncomment the following definition:
# def spiralOrder(matrix: List[List[int]]) -> List[int]:
#     ...

class TestSpiralOrder(unittest.TestCase):
    def test_example1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_example2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_example3(self):
        matrix = [[7],[9],[6]]
        expected = [7,9,6]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_single_row(self):
        matrix = [[1,2,3,4,5]]
        expected = [1,2,3,4,5]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_single_column(self):
        matrix = [[1],[2],[3],[4]]
        expected = [1,2,3,4]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_single_element(self):
        matrix = [[42]]
        expected = [42]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_two_by_two(self):
        matrix = [[1,2],[3,4]]
        expected = [1,2,4,3]
        self.assertEqual(spiralOrder(matrix), expected)

    def test_three_by_four(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(spiralOrder(matrix), expected)

if __name__ == '__main__':
    unittest.main()