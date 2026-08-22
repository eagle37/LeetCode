# Last updated: 8/22/2026, 6:26:03 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        d = ""
        for i in range(len(strs[0])):
            cur = strs[0][i]
            for j in range(1,len(strs)):
                if (i>=len(strs[j])) or (strs[j][i]!=cur):
                    return d
            d+=cur
        return d
