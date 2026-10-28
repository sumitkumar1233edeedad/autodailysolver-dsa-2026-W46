import unittest
from typing import List

# Import the solution function (assuming it's in the same module)
# In a real scenario, you might import from a module, but here we define it again for completeness.
# We'll just copy the function here to make the test self-contained.
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

class TestRotateImage(unittest.TestCase):
    def test_example1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_example2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_single_element(self):
        matrix = [[1]]
        expected = [[1]]
        rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_two_by_two(self):
        matrix = [[1,2],[3,4]]
        expected = [[3,1],[4,2]]
        rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_four_by_four_another(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        rotate(matrix)
        self.assertEqual(matrix, expected)
    
    def test_in_place_modification(self):
        matrix = [[1,2],[3,4]]
        original_id = id(matrix)
        rotate(matrix)
        self.assertEqual(id(matrix), original_id, "Matrix should be modified in-place, not replaced")
        # Also check that the content changed
        self.assertEqual(matrix, [[3,1],[4,2]])

if __name__ == '__main__':
    unittest.main()
