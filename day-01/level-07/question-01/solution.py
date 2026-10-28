from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Rotates the given n x n matrix 90 degrees clockwise in-place.

    The algorithm first transposes the matrix (swap matrix[i][j] with matrix[j][i] for i < j),
    then reverses each row.

    Args:
        matrix: A list of n lists, each of length n, representing the image.

    Returns:
        None. The matrix is modified in-place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
