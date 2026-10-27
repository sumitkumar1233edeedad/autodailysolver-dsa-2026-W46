# Longest Subarray with At Most K Distinct Integers

- **Day:** `Day 01`
- **Level:** `Level 04`
- **Question:** `Question 02`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return the length of the longest contiguous subarray that contains at most `k` distinct integers.

A subarray is a contiguous part of an array.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= k <= nums.length

**Example 1:**
Input: nums = [1,2,1,2,3], k = 2
Output: 4
Explanation: The longest subarray with at most 2 distinct integers is [1,2,1,2] with length 4.

**Example 2:**
Input: nums = [1,2,3,4,5], k = 1
Output: 1
Explanation: The longest subarray with at most 1 distinct integer is any single element, length 1.

**Example 3:**
Input: nums = [1,1,1,1,1], k = 2
Output: 5
Explanation: The entire array has only 1 distinct integer, which is <= 2, so length 5.

---

## 💻 Starter Function

```python
from typing import List

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problem (Minimum Size Subarray Sum) practiced variable-size sliding window with a sum condition (>= target) on positive numbers, focusing on minimizing window length. This problem introduces a complementary twist: instead of a sum constraint, we have a distinct-element constraint (at most k distinct), which requires a hash map to track frequencies within the window. This shifts the focus from arithmetic accumulation to frequency counting and direct indexing, reinforcing the Arrays & Hashing theme. The sliding window technique is adapted to maintain a valid window by expanding the right pointer and contracting the left pointer when distinct count exceeds k, optimizing for maximum window length (vs minimum previously). This dual-pointer variation with a hash map for boundary management is a core pattern for subarray problems with cardinality constraints. It avoids duplication by using a frequency-map-based condition rather than a sum-based condition, and by maximizing length instead of minimizing.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
