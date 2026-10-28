# Maximum Weight Overlap Intervals

- **Day:** `Day 01`
- **Level:** `Level 08`
- **Question:** `Question 01`
- **Difficulty:** `Hard`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

You are given a list of weighted intervals, where each interval is represented as `[start, end, weight]`. The interval covers all real numbers `t` such that `start <= t < end` (half-open interval). The **weight** of a time point `t` is the sum of weights of all intervals that contain `t`.

Your task is to find the **maximum weight** (peak) across all time points, and return all **maximal contiguous half-open intervals** where this peak weight is achieved. The result should be a list of disjoint intervals `[start, end]` sorted by `start` time. If two peak intervals are adjacent (e.g., `[1,3)` and `[3,5)`), they should be merged into a single interval `[1,5)`.

### Constraints
- `1 <= intervals.length <= 10^5`
- `0 <= start < end <= 10^9`
- `1 <= weight <= 10^4`
- Intervals are half-open `[start, end)`.

### Examples
**Example 1**
```
Input: intervals = [[1,5,2],[2,6,3],[4,7,1]]
Output: [[4,5]]
Explanation:
Time 1: weight 2
Time 2-4: weight 2+3=5
Time 4: weight 2+3+1=6 (peak)
Time 5: weight 3+1=4
Time 6: weight 1
The maximum weight is 6, occurring only in the half-open interval [4,5).
```

**Example 2**
```
Input: intervals = [[1,3,1],[4,6,1],[7,9,1]]
Output: [[1,3],[4,6],[7,9]]
Explanation: The maximum weight is 1, achieved in three separate intervals with gaps between them.
```

**Example 3**
```
Input: intervals = [[1,10,5],[2,3,2],[4,5,2],[6,7,2]]
Output: [[2,3],[4,5],[6,7]]
Explanation: The maximum weight is 7 (5+2), achieved in three separate intervals where the small intervals overlap the large one.
```

---

## 💻 Starter Function

```python
from typing import List

def find_peak_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Returns the list of maximal contiguous half-open intervals where the weight sum is maximum.
    """
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> Previous problems in this curriculum have covered linear traversals, two-pointer techniques, sliding windows, hash-based frequency counting, and matrix manipulations. This problem introduces the canonical sweep-line algorithm for interval processing, which is a core mechanic for 'Intervals & Extremes'. It requires sorting events (start/end points) and using a hash map (or coordinate compression) to handle large coordinate ranges efficiently, fitting the 'Arrays & Hashing' topic. The weighted overlap tracking extends the classic meeting-rooms/merge-intervals pattern by adding a weight dimension and requiring the extraction of all peak segments, making it a Hard-level challenge that avoids duplication of any prior problem while reinforcing the fundamental interval sweep-line pattern.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
