# Move Zeroes

- **Day:** `Day 01`
- **Level:** `Level 03`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

**Examples:**

**Example 1:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Example 2:**
```
Input: nums = [0]
Output: [0]
```

**Example 3:**
```
Input: nums = [1,2,3]
Output: [1,2,3]
```

---

## 💻 Starter Function

```python
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'Remove Duplicates from Sorted Array' (Level 03 Q01) used a slow/fast two-pointer technique to overwrite duplicates in a sorted array, where the invariant was 'elements before slow are unique'. This problem 'Move Zeroes' is the perfect complementary twist: it also uses a slow/fast two-pointer approach in-place, but the invariant shifts to 'elements before slow are non-zero'. The fast pointer scans for non-zero values to swap/assign to the slow pointer, then zeros out the tail. This reinforces the core in-place two-pointer pattern while changing the condition (value != 0 vs nums[fast] != nums[slow-1]) and the post-processing step (filling zeros vs truncating length). It avoids duplicate mechanics by targeting a different rearrangement goal (partitioning vs deduplication) and works on unsorted input, broadening the student's toolkit for in-place array mutations.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
