# Find Target Index in Array

- **Day:** `Day 02`
- **Level:** `Level 01`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return the index of the **first occurrence** of `target` in `nums`. If `target` does not exist in the array, return `-1`.

You must solve this problem using a simple linear scan (iterating through the array once).

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i], target <= 10^9`

**Example 1:**
```
Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
Output: 4
Explanation: The value 0 appears at index 4 (0-based).
```

**Example 2:**
```
Input: nums = [10, 20, 30, 40], target = 25
Output: -1
Explanation: 25 is not present in the array.
```

**Example 3:**
```
Input: nums = [5, 5, 5, 5], target = 5
Output: 0
Explanation: The first occurrence of 5 is at index 0.
```

---

## 💻 Starter Function

```python
from typing import List

def find_target_index(nums: List[int], target: int) -> int:
    """
    Returns the index of the first occurrence of target in nums.
    If target is not found, returns -1.
    """
    # Your code here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous curriculum (Day 01) covered advanced array/hashing problems up to Hard difficulty, including sliding windows, two pointers, and complex frequency analyses. Day 02 Level 01 Question 01 resets to the foundational building block: linear traversal and direct element search. This problem isolates the core mechanic of scanning an array sequentially to locate a target value, reinforcing index manipulation, loop control, and early termination. It avoids duplication by not using hash sets, frequency counters, or sorted properties—just a raw linear scan—making it the canonical 'first algorithm' for array search. The next questions in this level can then build upon this by introducing hash-based lookups or two-pointer techniques.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
