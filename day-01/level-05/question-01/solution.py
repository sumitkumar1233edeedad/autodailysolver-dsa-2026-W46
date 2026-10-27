from collections import defaultdict
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    """
    Returns the total number of continuous subarrays whose sum equals to k.

    Uses a prefix sum hashmap to store the frequency of each prefix sum encountered.
    For each current prefix sum, we check how many previous prefix sums equal (current - k),
    which corresponds to subarrays ending at the current index with sum k.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # empty prefix sum
    current_sum = 0
    count = 0
    for num in nums:
        current_sum += num
        # If there is a prefix sum equal to current_sum - k, then the subarray between that prefix and current index sums to k.
        count += prefix_counts.get(current_sum - k, 0)
        prefix_counts[current_sum] += 1
    return count