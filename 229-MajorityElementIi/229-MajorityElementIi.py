# Last updated: 9/12/2026, 1:02:46 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        count1 = count2 = 0

        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 = 1
            elif count2 == 0:
                c2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Candidates are not necessarily actual majorities
        count1 = count2 = 0

        for num in nums:
            if num == c1:
                count1 += 1
            elif num == c2:
                count2 += 1

        ans = []

        if count1 > len(nums) // 3:
            ans.append(c1)

        if count2 > len(nums) // 3:
            ans.append(c2)

        return ans