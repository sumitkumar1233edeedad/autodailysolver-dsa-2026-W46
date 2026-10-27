from typing import List

def max_prefix_suffix_sum(nums: List[int]) -> int:
    """
    Returns the maximum sum of a non-overlapping prefix and suffix of the array.
    The prefix and suffix can be empty. If all numbers are negative, returns 0.

    Args:
        nums: List of integers.

    Returns:
        Maximum possible sum of selected prefix and suffix.
    """
    total = sum(nums)
    prefix = 0
    max_prefix = 0
    ans = 0
    n = len(nums)
    for j in range(n + 1):
        # At this point, prefix = sum(nums[0:j]), max_prefix = max_{0 <= i <= j} sum(nums[0:i])
        candidate = max_prefix + total - prefix
        if candidate > ans:
            ans = candidate
        if j < n:
            prefix += nums[j]
            if prefix > max_prefix:
                max_prefix = prefix
    return ans
