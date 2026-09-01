# Last updated: 9/01/2026, 11:28:28 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        s = 0
        k = 1
        for i in digits[::-1]:
            s += i * k
            k *= 10
        s += 1
        j = -1
        li = []
        while s > 0:
            d = s % 10
            s = s // 10
            li.insert(j, d)
            j -= 1
        return li
