from bisect import bisect_left

def maximumWeight(intervals):
    n = len(intervals)

    # Store: (left, right, weight, original_index)
    arr = []

    for i, (l, r, w) in enumerate(intervals):
        arr.append((l, r, w, i))

    # Sort by ending position
    arr.sort(key=lambda x: (x[1], x[3]))

    # Ending positions
    ends = [x[1] for x in arr]

    # Find the previous non-overlapping interval
    prev = [0] * n

    for i in range(n):
        # Need previous right < current left
        j = bisect_left(ends, arr[i][0]) - 1
        prev[i] = j + 1

    # dp[k][i] = best answer using first i intervals
    # and choosing at most k intervals
    dp = [[(0, []) for _ in range(n + 1)] for _ in range(5)]

    for k in range(1, 5):
        for i in range(1, n + 1):

            # Do not choose current interval
            not_take = dp[k][i - 1]

            # Choose current interval
            old_score, old_indices = dp[k - 1][prev[i - 1]]

            new_index = arr[i - 1][3]
            new_score = old_score + arr[i - 1][2]

            new_indices = old_indices + [new_index]
            new_indices.sort()

            take = (new_score, new_indices)

            # Choose better score
            if take[0] > not_take[0]:
                dp[k][i] = take

            elif take[0] < not_take[0]:
                dp[k][i] = not_take

            else:
                # Same score -> lexicographically smaller
                if take[1] < not_take[1]:
                    dp[k][i] = take
                else:
                    dp[k][i] = not_take

    return dp[4][n][1]


# Example 1
intervals = [
    [1, 3, 2],
    [4, 5, 2],
    [1, 5, 5],
    [6, 9, 3],
    [6, 7, 1],
    [8, 9, 1]
]

print(maximumWeight(intervals))


# Example 2
intervals = [
    [5, 8, 1],
    [6, 7, 7],
    [4, 7, 3],
    [9, 10, 6],
    [7, 8, 2],
    [11, 14, 3],
    [3, 5, 5]
]

print(maximumWeight(intervals))
