from typing import List
from collections import defaultdict

def longest_subarray_at_most_k_distinct(nums: List[int], k: int) -> int:
    """
    Returns the length of the longest contiguous subarray with at most k distinct integers.
    Uses sliding window with a hash map to track counts of elements in the current window.
    Time Complexity: O(n), where n is len(nums).
    Space Complexity: O(k) for the hash map (at most k+1 distinct elements stored).
    """
    if k == 0:
        return 0
    left = 0
    max_len = 0
    count = defaultdict(int)
    distinct = 0
    for right, num in enumerate(nums):
        if count[num] == 0:
            distinct += 1
        count[num] += 1
        while distinct > k:
            left_num = nums[left]
            count[left_num] -= 1
            if count[left_num] == 0:
                distinct -= 1
            left += 1
        # now distinct <= k
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len
