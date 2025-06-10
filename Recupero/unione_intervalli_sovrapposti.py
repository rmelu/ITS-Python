def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Check if there is an overlap
        if current[0] <= last_merged[1]:
            # Merge the intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add the current interval
            merged.append(current)

    return merged

print(merge_intervals([[1, 3], [2, 4], [5, 7], [6, 8]]))  # Output: [[1, 4], [5, 8]]
print(merge_intervals([[1, 2], [3, 4], [5, 6]]))  # Output: [[1, 2], [3, 4], [5, 6]]
print(merge_intervals([[1, 5], [2, 3], [4, 6]]))  # Output: [[1, 6]]
print(merge_intervals([[1, 10], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 10], [15, 18]]