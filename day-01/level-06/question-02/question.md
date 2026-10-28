# Partition Array by Frequency Threshold

- **Day:** `Day 01`
- **Level:** `Level 06`
- **Question:** `Question 02`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, partition the array **in-place** such that all elements with a frequency **strictly greater than** `k` appear before all elements with a frequency **less than or equal to** `k`.

The relative order of elements within each partition does **not** need to be preserved.

You must solve the problem in `O(n)` time complexity and `O(n)` additional space (for frequency counting), while performing the partitioning in-place (i.e., `O(1)` extra space apart from the frequency map).

---

### Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= nums.length`

---

### Example 1
**Input:** `nums = [1,2,3,1,2,4], k = 1`
**Output:** `[1,2,1,2,3,4]` (or any permutation where `1` and `2` precede `3` and `4`)
**Explanation:** Frequencies: `1->2`, `2->2`, `3->1`, `4->1`. Elements with frequency > 1 are `1` and `2`. They are moved to the front.

### Example 2
**Input:** `nums = [5,5,5,5], k = 2`
**Output:** `[5,5,5,5]`
**Explanation:** Frequency of `5` is 4 (>2). All elements already satisfy the condition.

### Example 3
**Input:** `nums = [10,20,30], k = 0`
**Output:** `[10,20,30]`
**Explanation:** Every element appears once, which is > 0. No rearrangement needed.

---

## 💻 Starter Function

```python
from typing import List

def partition_by_frequency(nums: List[int], k: int) -> List[int]:
    """
    Partitions nums in-place so that elements with frequency > k come first.
    Returns the modified nums.
    """
    # Your code here
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'Top K Frequent Elements' (Level 06 Q01) reinforced frequency analysis using bucket sort, while 'Partition Array by Value Range' (Level 06 Q02) practiced three-way in-place partitioning based on a static value range. This new problem creates a complementary twist by combining both concepts: it requires a hash map to dynamically determine the partition predicate (frequency > k) and then applies a classic two-pointer in-place partitioning pass. This reinforces the pattern of using auxiliary data structures (hashing) to define partition criteria, followed by linear in-place rearrangement (dual-pointer), which is a core skill for array manipulation under linear traversal constraints.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
