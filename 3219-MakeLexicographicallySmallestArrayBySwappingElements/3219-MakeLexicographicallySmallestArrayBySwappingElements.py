# Last updated: 9/4/2026, 3:23:17 PM
class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        arr = sorted((num, i) for i, num in enumerate(nums))

        i = 0

        while i < n:
            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for k in range(len(indices)):
                nums[indices[k]] = arr[i + k][0]

            i = j + 1

        return nums