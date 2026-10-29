# Remove Duplicates from Unsorted Array In-Place

- **Day:** `Day 02`
- **Level:** `Level 02`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array `nums`. More formally, if there are `k` unique elements after removing duplicates, then the first `k` elements of `nums` should hold the unique elements in the order they were present originally. Return `k` after placing the final result in the first `k` slots of `nums`.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory (excluding the hash set used for tracking seen elements).

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

**Example 1:**
Input: nums = [1,2,3,2,4,1]
Output: 4, nums = [1,2,3,4,_,_]
Explanation: The unique elements are [1,2,3,4]. The first 4 elements of nums are modified to 1,2,3,4. The remaining elements are not important.

**Example 2:**
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: The unique elements are [0,1,2,3,4].

**Example 3:**
Input: nums = [5,5,5,5]
Output: 1, nums = [5,_,_,_]

---

## 💻 Starter Function

```python
def remove_duplicates(nums: List[int]) -> int:
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem 'Sum of Unique Elements' practiced frequency counting with a hash map to compute a sum. This problem shifts to an in-place modification using a hash set for membership tracking and a dual-pointer (read/write) technique to compact the array. It reinforces hash set usage while introducing the critical pattern of in-place array transformation with O(1) extra space (aside from the set). This avoids duplication of the summation mechanic and instead focuses on array mutation and pointer manipulation, a complementary skill for array-hashing problems.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
