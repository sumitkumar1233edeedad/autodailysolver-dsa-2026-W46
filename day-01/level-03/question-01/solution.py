from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    Removes duplicates from a sorted array in-place and returns the number of unique elements.
    
    Args:
        nums: List of integers sorted in non-decreasing order.
        
    Returns:
        The number of unique elements (k). The first k elements of nums will contain the unique elements.
    """
    if not nums:
        return 0
    
    # slow pointer points to the last unique element's position
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    # Number of unique elements is slow + 1
    return slow + 1