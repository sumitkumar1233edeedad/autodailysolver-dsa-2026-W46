# Contains Duplicate

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

**Example 1:**
- Input: `nums = [1,2,3,1]`
- Output: `true`
- Explanation: The value `1` appears at indices 0 and 3.

**Example 2:**
- Input: `nums = [1,2,3,4]`
- Output: `false`
- Explanation: All elements are distinct.

**Example 3:**
- Input: `nums = [1,1,1,3,3,4,3,2,4,2]`
- Output: `true`
- Explanation: Multiple values (`1`, `3`, `4`, `2`) appear more than once.

---

## 💻 Starter Function

```python
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous level (Level 01) focused on Linear Traversal & Search, likely solving problems via brute-force iteration or simple single-pass logic without auxiliary data structures. This problem (Level 02, Q01) introduces the Hash Set as the canonical tool for 'Frequency & Hash Sets'. It teaches the fundamental pattern of trading space (O(n)) for time (O(n)) to solve duplicate detection, moving away from O(n^2) nested loops or O(n log n) sorting. It establishes the core 'visit and record' mechanic using a set for O(1) average-case lookups, which is the prerequisite for all subsequent frequency counting and hashing problems in this level.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
