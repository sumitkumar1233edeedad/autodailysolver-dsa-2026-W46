# In-Place Merge Intervals for Maximum Weight

- **Day:** `Day 01`
- **Level:** `Level 08`
- **Question:** `Question 02`
- **Difficulty:** `Hard`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

You are given an array `intervals` where `intervals[i] = [start_i, end_i, weight_i]`. The array is **sorted in non-decreasing order by `start_i`**.

Merge all overlapping intervals **in-place** such that the first `k` elements of `intervals` contain the merged intervals. A merged interval is defined as:
- `start` = minimum start of the overlapping group
- `end` = maximum end of the overlapping group
- `weight` = sum of weights of all intervals in the overlapping group

Two intervals overlap if they share at least one common point (i.e., `start1 <= end2 && start2 <= end1`). After merging, the merged intervals must be non-overlapping and remain sorted by start time.

Return the **maximum weight** among all merged intervals.

**Constraints:**
- `1 <= intervals.length <= 10^5`
- `0 <= start_i <= end_i <= 10^9`
- `1 <= weight_i <= 10^4`
- The input array is sorted by `start_i`.
- **You must solve this in-place with O(1) extra space** (excluding the output variable).

**Example 1:**
```
Input: intervals = [[1,3,5],[2,6,3],[8,10,2],[15,18,4]]
Output: 8
Explanation: Merge [1,3,5] and [2,6,3] into [1,6,8]. The merged intervals are [[1,6,8],[8,10,2],[15,18,4]]. Maximum weight is 8.
```

**Example 2:**
```
Input: intervals = [[1,4,2],[4,5,3]]
Output: 5
Explanation: Intervals overlap at 4. Merged into [1,5,5]. Maximum weight is 5.
```

**Example 3:**
```
Input: intervals = [[1,2,1],[3,4,2],[5,6,3]]
Output: 3
Explanation: No overlaps. Maximum weight is 3.
```

---

## 💻 Starter Function

```python
from typing import List

def max_weight_merged_intervals(intervals: List[List[int]]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'Maximum Weight Overlap Intervals' (Level 08 Q01) practiced the sweep-line pattern to find the maximum weight of intervals overlapping at a single point. The complementary twist for Part 2 is 'in-place constraints' on interval merging. This problem requires merging overlapping intervals in-place (O(1) space) while accumulating weights, and then finding the maximum weight among the merged intervals. It reinforces the two-pointer pattern for in-place array modification and interval merging, which is a fundamental skill for array problems. It avoids duplication by focusing on the merging process rather than just querying overlap weights, and it introduces the constraint of in-place transformation which is a common follow-up in interviews.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
