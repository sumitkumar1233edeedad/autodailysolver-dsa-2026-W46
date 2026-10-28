from typing import List

def max_weight_merged_intervals(intervals: List[List[int]]) -> int:
    """
    Merges overlapping intervals in-place and returns the maximum weight among merged intervals.

    Args:
        intervals: A list of intervals [start, end, weight], sorted by start in non-decreasing order.

    Returns:
        The maximum weight of any merged interval.
    """
    n = len(intervals)
    if n == 0:
        return 0

    write_idx = 0
    cur_start, cur_end, cur_weight = intervals[0]
    max_weight = cur_weight

    for i in range(1, n):
        nxt_start, nxt_end, nxt_weight = intervals[i]
        if nxt_start <= cur_end:  # Overlap
            cur_end = max(cur_end, nxt_end)
            cur_weight += nxt_weight
            if cur_weight > max_weight:
                max_weight = cur_weight
        else:
            # Write the merged interval
            intervals[write_idx] = [cur_start, cur_end, cur_weight]
            write_idx += 1
            # Start new interval
            cur_start, cur_end, cur_weight = nxt_start, nxt_end, nxt_weight
            if cur_weight > max_weight:
                max_weight = cur_weight

    # Write the last merged interval
    intervals[write_idx] = [cur_start, cur_end, cur_weight]
    # The first write_idx + 1 elements now contain the merged intervals.

    return max_weight