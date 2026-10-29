from collections import Counter
from typing import List

def sum_of_unique(nums: List[int]) -> int:
    """
    Returns the sum of all unique elements in the array.
    An element is unique if it appears exactly once.

    Args:
        nums: List of integers.

    Returns:
        Sum of unique elements.
    """
    freq = Counter(nums)
    return sum(num for num, count in freq.items() if count == 1)