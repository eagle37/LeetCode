# Last updated: 8/15/2026, 4:32:44 PM
class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        st = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in d:
                st.append(i)
            else:
                if not st:
                    return False
                if d[st[-1]] == i:
                    st.pop()
                else:
                    return False
        return len(st) == 0
                    