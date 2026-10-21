# Last updated: 10/21/2026, 9:31:32 PM
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        d = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []

        for i in words:
            r = None

            for j in i.lower():
                if r is None:
                    if j in d[0]:
                        r = 0
                    elif j in d[1]:
                        r = 1
                    else:
                        r = 2
                elif j not in d[r]:
                    break
            else:
                ans.append(i)

        return ans