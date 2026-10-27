def moveZeroes(nums: list[int]) -> None:
    """
    Moves all zeros in the list to the end while maintaining the relative order of non-zero elements.
    This is done in-place with O(n) time complexity and O(1) space complexity.

    Args:
        nums: List of integers to be modified in-place.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
