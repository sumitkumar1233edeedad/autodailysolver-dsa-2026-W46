from typing import List


def partition_by_frequency(nums: List[int], k: int) -> List[int]:
    """
    Partitions nums in-place so that elements with frequency > k come first.
    Returns the modified nums.
    """
    if not nums:
        return nums
    
    # Count frequencies
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # Two-pointer in-place partition
    left, right = 0, len(nums) - 1
    while left <= right:
        if freq[nums[left]] > k:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    
    return nums
