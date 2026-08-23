# Last updated: 8/23/2026, 6:30:15 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        rs = []

        def backtrack(pos, curr):
            if pos == len(digits):
                rs.append(curr)
                return
            for ch in d[digits[pos]]:
                backtrack(pos+1, curr+ch)
        backtrack(0, "")
        return rs