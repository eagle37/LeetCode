# Last updated: 8/29/2026, 8:27:17 PM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        permutations = []
        current_permutation = []
        used = [False] * n

        def backtrack():
            if len(current_permutation) == n:
                permutations.append(current_permutation.copy())
                return

            for i in range(n):
                if used[i]:
                    continue

                # nums[i] を今回の順列に追加する
                used[i] = True
                current_permutation.append(nums[i])

                backtrack()

                # 選択前の状態に戻す
                current_permutation.pop()
                used[i] = False

        backtrack()
        return permutations