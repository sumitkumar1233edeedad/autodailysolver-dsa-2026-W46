from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Return the k most frequent elements in nums.
    Uses bucket sort to achieve O(n) time complexity.
    """
    # Count frequencies
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1
    
    # Create buckets: index = frequency, value = list of numbers with that frequency
    max_freq = len(nums)
    buckets = [[] for _ in range(max_freq + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)
    
    # Collect top k frequent elements
    result = []
    for freq in range(max_freq, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result
