# Subarray Sum Equals K

- **Day:** `Day 01`
- **Level:** `Level 05`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

**Constraints:**
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

**Example 1:**
```
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays [1,1] (indices 0-1) and [1,1] (indices 1-2) sum to 2.
```

**Example 2:**
```
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3] sum to 3.
```

**Example 3:**
```
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: Subarrays [1,-1], [-1,0], [1,-1,0] sum to 0.
```

---

## 💻 Starter Function

```python
def subarraySum(nums: list[int], k: int) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous Level 04 problems (Minimum Size Subarray Sum, Longest Subarray with At Most K Distinct) utilized Sliding Window techniques with HashMaps for tracking window state. Level 05 introduces Prefix & Suffix Transforms. 'Subarray Sum Equals K' is the canonical problem bridging HashMaps (topic requirement) with Prefix Sums (pattern requirement). It shifts the paradigm from maintaining a valid window (two pointers) to calculating cumulative prefix sums and using a HashMap to count occurrences of `prefix_sum - k`, efficiently handling negative numbers which break standard sliding window logic. This avoids duplication of 'Minimum Size Subarray Sum' (which finds min length, often positive integers only) by focusing on counting *all* valid subarrays in a general integer array.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
