# Last updated: 8/23/2026, 6:11:28 PM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        d = {
4            "2": "abc", 
5            "3": "def", 
6            "4": "ghi", 
7            "5": "jkl", 
8            "6": "mno",
9            "7": "pqrs",
10            "8": "tuv",
11            "9": "wxyz"
12        }
13
14        rs = []
15
16        def backtrack(pos, curr):
17            if pos == len(digits):
18                rs.append(curr)
19                return
20            for ch in d[digits[pos]]:
21                backtrack(pos+1, curr+ch)
22        backtrack(0, "")
23        return rs