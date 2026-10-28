from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Returns the elements of the given matrix in spiral order.

    Args:
        matrix: A 2D list of integers representing the matrix.

    Returns:
        A list of integers in spiral order.
    """
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse top row from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Traverse right column from top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Traverse bottom row from right to left, if there is a remaining row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Traverse left column from bottom to top, if there is a remaining column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result