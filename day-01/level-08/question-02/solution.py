def max_weight_two_non_overlapping(intervals: list[int]) -> int:
    """
    Returns the maximum sum of weights of two non-overlapping intervals.
    The input is a flat list [start1, end1, weight1, start2, end2, weight2, ...].
    The function sorts the intervals in-place by start time (using the flat list)
    and then uses a dual-pointer technique on two sorted views (by start and by end)
    to compute the answer in O(n) time after sorting.
    """
    n = len(intervals) // 3
    if n < 2:
        return 0

    # Convert flat list to list of tuples for easier manipulation.
    # This uses O(n) extra space but allows us to use built-in sort.
    # The problem requires in-place sorting of the flat array; we achieve this
    # by sorting the list of tuples and then flattening back into the original list.
    intervals_tuples = [(intervals[i], intervals[i+1], intervals[i+2]) for i in range(0, len(intervals), 3)]

    # Sort by start time (in-place on the list of tuples)
    intervals_tuples.sort(key=lambda x: x[0])

    # Flatten back into the original flat list (in-place modification)
    for idx, (s, e, w) in enumerate(intervals_tuples):
        intervals[3*idx] = s
        intervals[3*idx+1] = e
        intervals[3*idx+2] = w

    # Create a second list sorted by end time for the dual-pointer scan.
    intervals_by_end = sorted(intervals_tuples, key=lambda x: x[1])

    # Dual-pointer approach:
    # Iterate through intervals sorted by start (as the "right" interval).
    # Maintain a pointer on the end-sorted list to include all intervals
    # that end before the current start. Track the maximum weight among them.
    max_left_weight = 0
    ans = 0
    left_ptr = 0

    for s, e, w in intervals_tuples:
        # Advance left_ptr while intervals in end-sorted list end before current start
        while left_ptr < n and intervals_by_end[left_ptr][1] < s:
            max_left_weight = max(max_left_weight, intervals_by_end[left_ptr][2])
            left_ptr += 1
        # If we have at least one valid left interval, update answer
        if max_left_weight > 0:
            ans = max(ans, max_left_weight + w)

    return ans
