# Maximum Sum of Non-Overlapping Prefix and Suffix

- **Day:** `Day 01`
- **Level:** `Level 05`
- **Question:** `Question 02`
- **Difficulty:** `Medium`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, you want to select a **prefix** (possibly empty) and a **suffix** (possibly empty) such that they do not overlap. The selected elements are the union of the prefix and the suffix. Your goal is to maximize the sum of the selected elements.

Formally, choose indices `i` and `j` with `0 <= i <= j <= n` (where `n` is the length of `nums`). The prefix is `nums[0..i-1]` and the suffix is `nums[j..n-1]`. The sum is `sum(nums[0..i-1]) + sum(nums[j..n-1])`. Maximize this sum.

Return the maximum possible sum.

**Note:** The prefix and suffix can be empty (sum 0). If all numbers are negative, the best is to choose empty prefix and empty suffix, giving a sum of 0.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

**Example 1:**
```
Input: nums = [1, -2, 3, -4, 5]
Output: 7
Explanation: Choose prefix [1, -2, 3] (sum = 2) and suffix [5] (sum = 5). Total = 7.
```

**Example 2:**
```
Input: nums = [-1, -2, -3]
Output: 0
Explanation: Choose empty prefix and empty suffix. Sum = 0.
```

**Example 3:**
```
Input: nums = [2, 3, -1, 4, -2, 5]
Output: 13
Explanation: Choose prefix [2, 3, -1, 4] (sum = 8) and suffix [5] (sum = 5). Total = 13.
```

---

## 💻 Starter Function

```python
def max_prefix_suffix_sum(nums: List[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous two problems (Product of Array Except Self and Trapping Rain Water) both used prefix/suffix transforms: the first computed prefix/suffix products, the second used prefix/suffix maximums with a two-pointer sweep. This problem is the logical next step because it keeps the prefix/suffix paradigm but introduces a complementary twist: we must maximize the combined sum of a prefix and a suffix that are disjoint. This requires computing prefix maximum sums and suffix maximum sums, then finding the optimal split point (edge boundary optimization) where the two segments meet without overlapping. It avoids duplicating mechanics (no product, no water trapping, no sliding window with distinct counts) while reinforcing the core pattern of building auxiliary prefix/suffix arrays and combining them with a linear scan or dual-pointer technique. The in-place constraint is optional but can be encouraged by reusing the input array for prefix sums.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
