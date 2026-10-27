# Product of Array Except Self

- **Day:** `Day 01`
- **Level:** `Level 05`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Constraints:**
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

**Example 1:**
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Example 2:**
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Example 3:**
```
Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

---

## 💻 Starter Function

```python
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous Level 04 problems ('Minimum Size Subarray Sum', 'Longest Subarray with At Most K Distinct Integers') established mastery of Sliding Window and Hash-map frequency tracking for subarray properties. Level 05 introduces Prefix & Suffix Transforms as the core pattern. 'Product of Array Except Self' is the canonical algorithmic entry point for this pattern: it requires computing prefix products (running product from left) and suffix products (running product from right) to decouple the dependency of `answer[i]` on the entire array. This teaches the fundamental mechanic of 'pre-computation into auxiliary arrays/variables' to achieve O(N) time without division, directly satisfying the 'Prefix & Suffix Transforms - Part 1 (Core Mechanics)' learning objective. It avoids duplication by shifting from window/frequency logic to positional accumulation logic.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
