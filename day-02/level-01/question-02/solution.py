def partition_by_sign(nums: list[int]) -> list[int]:
    """
    Rearranges nums in-place so that all negative numbers come before non-negative numbers.
    Returns the modified list.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        # Find the first non-negative from the left
        while left < right and nums[left] < 0:
            left += 1
        # Find the first negative from the right
        while left < right and nums[right] >= 0:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    return nums
