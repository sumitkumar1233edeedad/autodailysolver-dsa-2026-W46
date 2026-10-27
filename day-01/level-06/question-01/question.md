# Top K Frequent Elements

- **Day:** `Day 01`
- **Level:** `Level 06`
- **Question:** `Question 01`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**. 

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, number of unique elements in the array]`.
- It is **guaranteed** that the answer is unique.

**Follow-up:** Your algorithm's time complexity must be better than `O(n log n)`, where `n` is the array's size.

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

**Example 3:**
```
Input: nums = [4,1,-1,2,-1,2,3], k = 2
Output: [-1,2] (or [2,-1])
Explanation: -1 and 2 both appear twice. 4, 1, 3 appear once.
```

---

## 💻 Starter Function

```python
def topKFrequent(nums: list[int], k: int) -> list[int]:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems (Level 04-05) established Hash Map usage for counting/windowing (Longest Subarray K Distinct) and advanced array traversals (Prefix/Suffix Products/Sums). Level 06 introduces the **Selection Problem** paradigm via Partitioning (Quickselect). This problem is the canonical bridge: it requires a Hash Map for frequency counting (reinforcing Arrays & Hashing topic) followed by finding the Top K items. The optimal `O(N)` average time solution uses Quickselect partitioning on the unique elements array based on frequency, directly targeting the 'Quickselect partitioning' sub-pattern. It avoids duplication of sliding window, prefix/suffix, or simple two-pointer partitioning (Move Zeroes) mechanics.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
