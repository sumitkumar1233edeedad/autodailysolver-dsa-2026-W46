# First Unique Element in Array

- **Day:** `Day 01`
- **Level:** `Level 02`
- **Question:** `Question 02`
- **Difficulty:** `Easy`
- **Topic:** `Arrays & Hashing`
- **Status:** `Solved & Verified by AutoDailySolver Sandbox`

---

## 📝 Problem Statement

Given an integer array `nums`, return the **first element** that appears **exactly once** in the array. If no such element exists, return `-1`.

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

**Example 1:**
```
Input: nums = [2, 3, 4, 2, 3, 5]
Output: 4
Explanation: The elements 2 and 3 appear twice. The first element with frequency 1 is 4.
```

**Example 2:**
```
Input: nums = [1, 1, 2, 2, 3, 3]
Output: -1
Explanation: Every element appears at least twice, so there is no unique element.
```

**Example 3:**
```
Input: nums = [5]
Output: 5
Explanation: The single element is trivially unique.
```

---

## 💻 Starter Function

```python
from typing import List

def first_unique_element(nums: List[int]) -> int:
    pass
```

---

## 🧠 AI Auto-Think Pedagogical Reasoning

> The previous problem (Contains Duplicate) introduced the basic hash set pattern to detect any duplicate existence. This problem advances the frequency concept by requiring the identification of the first element with a frequency of exactly one. It reinforces hash map counting (frequency dictionary) and a second linear pass to respect the original order, which is a complementary twist on the same core pattern. It avoids duplication by shifting the goal from boolean existence to ordered retrieval, while staying within the Easy difficulty and the Frequency & Hash Sets sub-pattern.
---

## 📁 Files

- [`solution.py`](solution.py) — Optimal solution implementation.
- [`test_solution.py`](test_solution.py) — Comprehensive unit test suite.

*Automated, verified, and committed by [AutoDailySolver](https://github.com/sumitkumar1233edeedad/auto-daily-solver).*
