class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        pairs = []
        for i in range(n):
            pairs.append([nums[i], i])

        pairs.sort()

        ans = [0] * n
        start = 0

        while start < n:
            end = start

            while end + 1 < n:
                if pairs[end + 1][0] - pairs[end][0] <= limit:
                    end += 1
                else:
                    break

            indices = []
            for i in range(start, end + 1):
                indices.append(pairs[i][1])

            indices.sort()

            for i in range(len(indices)):
                ans[indices[i]] = pairs[start + i][0]

            start = end + 1

        return ans
