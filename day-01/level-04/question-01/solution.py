from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    """
    Returns the minimal length of a contiguous subarray of which the sum is 
    greater than or equal to target. If no such subarray exists, returns 0.
    
    Uses a sliding window approach with two pointers. Since all numbers are 
    positive, expanding the window increases the sum and shrinking it decreases 
    the sum, allowing us to find the minimal length in O(n) time.
    
    Args:
        target: The target sum (positive integer).
        nums: List of positive integers.
        
    Returns:
        Minimal length of subarray with sum >= target, or 0 if none exists.
    """
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(n):
        current_sum += nums[right]
        # Shrink the window from the left as long as the sum is >= target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return 0 if min_len == float('inf') else min_len