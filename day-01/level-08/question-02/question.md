# Maximum Weight of Two Non-Overlapping Intervals

- **Day:** `Day 01`
- **Level:** `Level 08`
- **Question:** `Question 02`
- **Difficulty:** `Hard`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

You are given a flat array `intervals` of length `3n` where each interval is represented by three consecutive integers: `start`, `end`, and `weight`. The intervals are not sorted. Your task is to find the maximum sum of weights of two non-overlapping intervals. Two intervals are non-overlapping if the end of one is strictly less than the start of the other (i.e., they do not share any point).

You must solve this problem by first sorting the intervals in-place by their start time (using O(1) extra space), then using a dual-pointer approach to compute the answer in O(n) time after sorting. Return the maximum sum of weights. If no two non-overlapping intervals exist, return 0.

**Constraints:**
- `2 <= n <= 10^5`
- `0 <= start < end <= 10^9`
- `1 <= weight <= 10^9`
- The array length is exactly `3n`.
- You must modify the array in-place for sorting (you may use built-in sort which is in-place).
- Extra space complexity must be O(1) excluding the input array.

**Example 1:**
```
Input: intervals = [1, 3, 5, 2, 4, 4, 5, 6, 3]
Interpretation: [[1,3,5], [2,4,4], [5,6,3]]
Output: 8
Explanation: Choose intervals [1,3,5] and [5,6,3] (non-overlapping because 3 < 5). Sum = 5 + 3 = 8.
```

**Example 2:**
```
Input: intervals = [1, 5, 10, 2, 3, 5, 4, 6, 8]
Interpretation: [[1,5,10], [2,3,5], [4,6,8]]
Output: 13
Explanation: Choose intervals [2,3,5] and [4,6,8] (non-overlapping because 3 < 4). Sum = 5 + 8 = 13.
```

**Example 3:**
```
Input: intervals = [1, 2, 5, 2, 3, 6]
Interpretation: [[1,2,5], [2,3,6]]
Output: 0
Explanation: The two intervals share the point 2 (end=2, start=2), so they overlap. No valid pair exists.
```

---

## 💻 Starter Function

```python
def max_weight_two_non_overlapping(intervals: list[int]) -> int:
    """
    Returns the maximum sum of weights of two non-overlapping intervals.
    The input is a flat list [start1, end1, weight1, start2, end2, weight2, ...].
    Must sort in-place and use dual-pointer technique.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Level 08 Q01) 'Maximum Weight Overlap Intervals' focused on finding a single point of maximum weight overlap using a sweep-line approach. This complementary twist shifts the focus to non-overlapping intervals: finding the maximum weight sum of two disjoint intervals. This requires sorting intervals by start time (in-place on a flat array) and then applying a dual-pointer (or two-pointer with binary search) technique to efficiently find the best pair. It reinforces interval sorting, in-place array manipulation, and dual-pointer traversal for extremes (maximum weight prefix/suffix), while avoiding duplication of the sweep-line mechanic. The flat-array representation adds an extra layer of index manipulation practice, aligning with the day's theme of Linear Traversals & Direct Indexing.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
