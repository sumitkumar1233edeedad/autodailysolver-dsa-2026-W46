from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Removes duplicates from an unsorted array in-place, preserving the relative order
    of the first occurrence of each unique element.

    Args:
        nums: List of integers (1 <= len(nums) <= 10^5).

    Returns:
        The number of unique elements (k). The first k elements of nums contain the
        unique elements in their original order.
    """
    seen = set()
    write = 0
    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[write] = num
            write += 1
    return write
