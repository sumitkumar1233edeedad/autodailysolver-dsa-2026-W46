# Remove Duplicates from Sorted Array

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The relative order of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
2. Return `k`.

**Constraints:**
- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

**Example 1:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 3:**
```
Input: nums = [1,1,1,1]
Output: 1, nums = [1,_,_,_]
```

---

## 💻 Starter Function

```python
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous Level 02 problems ('Contains Duplicate', 'First Unique Element') solved deduplication and frequency counting using Hash Sets/Maps, costing O(N) space. This Level 03 Q01 problem introduces the 'Two Pointers In-Place' pattern (Fast/Slow pointers) as the canonical optimization for *sorted* arrays. It teaches the core mechanic: the 'slow' pointer tracks the position of the last unique element (the write head), while the 'fast' pointer scans ahead (the read head) to find the next distinct value. This reinforces the algorithmic progression from 'Extra Space Lookup' -> 'In-Place Overwrite' leveraging the sorted property, a fundamental transition in array manipulation curricula.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
