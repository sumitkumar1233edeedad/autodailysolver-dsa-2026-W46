# Rotate Image

- **Day:** `Day 01`
- **Level:** `Level 07`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

You are given an `n x n` 2D `matrix` representing an image. Rotate the image by **90 degrees (clockwise)**.

You have to rotate the image **in-place**, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

### Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

### Examples

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2:**
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Example 3:**
```
Input: matrix = [[1]]
Output: [[1]]
```

---

## 💻 Starter Function

```python
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Levels 1-6) focused exclusively on 1D array manipulations: sliding windows, hash maps for frequency counting, prefix/suffix products, and two-pointer techniques. Level 7 introduces the fundamental shift to 2D matrix traversal mechanics. 'Rotate Image' is the canonical entry point for 2D matrix manipulation because it requires understanding layer-by-layer index mapping and in-place element swapping without extra space. It reinforces the core pattern of translating 1D traversal logic (loops, boundaries) into 2D coordinate transformations (row, col -> col, n-1-row). This problem avoids any hash-map or frequency logic, ensuring zero duplication with prior Array & Hashing questions while establishing the spatial reasoning needed for subsequent spiral and diagonal traversals.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
