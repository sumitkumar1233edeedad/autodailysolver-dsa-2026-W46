# Spiral Matrix

- **Day:** `Day 01`
- **Level:** `Level 07`
- **Question:** `Question 02`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

**Constraints:**
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Example 3:**
```
Input: matrix = [[7],[9],[6]]
Output: [7,9,6]
```

---

## 💻 Starter Function

```python
from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'Rotate Image' (Level 07 Q01) focused on in-place layer rotation using four-way element swaps. This problem, 'Spiral Matrix', is the complementary traversal counterpart: instead of modifying the matrix in layers, we read the matrix layer-by-layer in spiral order. It reinforces 2D matrix traversal patterns by requiring careful edge boundary optimization (shrinking top, bottom, left, right boundaries) and direction changes, which is a fundamental dual-pointer variation on 2D matrices. This avoids duplicating the in-place swap mechanics of rotation while deepening understanding of matrix layer boundaries and traversal control flow.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
