from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Returns an array where each element at index i is the product of all elements
    in nums except nums[i].

    This implementation runs in O(n) time and uses O(1) extra space (excluding
    the output array). It does not use division.

    Args:
        nums: List of integers with length >= 2.

    Returns:
        List of integers where answer[i] = product of all nums[j] for j != i.
    """
    n = len(nums)
    answer = [1] * n

    # Compute prefix products
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
