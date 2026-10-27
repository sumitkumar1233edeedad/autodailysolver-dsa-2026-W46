from typing import List
from collections import Counter

def first_unique_element(nums: List[int]) -> int:
    """
    Returns the first element in `nums` that appears exactly once.
    If no such element exists, returns -1.
    """
    freq = Counter(nums)
    for num in nums:
        if freq[num] == 1:
            return num
    return -1
