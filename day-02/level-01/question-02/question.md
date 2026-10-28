# Partition Array by Sign

- **Day:** `Day 02`
- **Level:** `Level 01`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, rearrange the elements **in-place** such that all negative numbers appear before all positive numbers. Zero is considered non‑negative and should be placed after the negatives. The relative order of the negative numbers and the positive numbers does **not** need to be preserved.

Return the modified array after partitioning.

**Constraints**
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- Must use `O(1)` extra space (in‑place).
- Time complexity: `O(n)`.

**Examples**

**Example 1**
```
Input: nums = [3, -1, -2, 4, 0, -5]
Output: [-1, -2, -5, 4, 0, 3]
Explanation: Any arrangement with all negatives before non‑negatives is accepted.
```

**Example 2**
```
Input: nums = [-1, 2, -3, 4]
Output: [-1, -3, 2, 4]
```

**Example 3**
```
Input: nums = [1, 2, 3]
Output: [1, 2, 3]
Explanation: No negative numbers, array remains unchanged.
```

---

## 💻 Starter Function

```python
def partition_by_sign(nums: list[int]) -> list[int]:
    """
    Rearranges nums in-place so that all negative numbers come before non-negative numbers.
    Returns the modified list.
    """
    # Your code here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Day 02 Level 01 Q01) practiced basic linear search to find a target index. This problem introduces the dual-pointer technique (left and right pointers) for in-place array partitioning, a fundamental linear traversal pattern. It reinforces edge boundary handling (pointers crossing) and in-place manipulation without extra space, complementing the simple search with a two-pointer mutation pattern. It avoids duplication by not using hash sets (saving that for later levels) and not overlapping with avoided problems like Move Zeroes or Remove Duplicates.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
