# Sum of Unique Elements

- **Day:** `Day 02`
- **Level:** `Level 02`
- **Question:** `Question 01`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return the sum of all **unique** elements in the array. An element is considered unique if it appears **exactly once** in the array.

**Constraints:**
- `1 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

**Example 1:**
```
Input: nums = [1, 2, 3, 2]
Output: 4
Explanation: The unique elements are 1 and 3. Their sum is 4.
```

**Example 2:**
```
Input: nums = [1, 1, 1, 1, 1]
Output: 0
Explanation: There are no unique elements.
```

**Example 3:**
```
Input: nums = [1, 2, 3, 4, 5]
Output: 15
Explanation: All elements are unique. Sum = 1+2+3+4+5 = 15.
```

---

## 💻 Starter Function

```python
def sum_of_unique(nums: list[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous Level 01 problems (Day 02) focused on linear traversal (find target index) and in-place partitioning (partition by sign). Level 02 introduces hash-based frequency counting. This problem is the canonical 'first contact' with a frequency map: we count occurrences of each value, then aggregate (sum) those with count == 1. It reinforces the core mechanic of building a hash map (dictionary) in a single pass and using it for a simple query, without overlapping with avoided problems like 'Contains Duplicate' (boolean existence), 'First Unique Element' (return first unique value), or 'Top K Frequent' (ranking). The summation twist ensures the student practices the full count-then-filter pattern.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
