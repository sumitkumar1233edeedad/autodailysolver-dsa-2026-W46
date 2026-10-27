from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Returns True if any value appears at least twice in the array, False otherwise.
    
    Args:
        nums: List of integers.
        
    Returns:
        True if there is a duplicate, False if all elements are distinct.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
