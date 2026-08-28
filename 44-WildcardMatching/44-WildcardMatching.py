# Last updated: 8/28/2026, 10:00:08 PM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        match_idx = 0

        while s_ptr < len(s):
            # 1. Direct character match or single character wildcard '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1

            # 2. Wildcard '*' found: record pointers for backtracking
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1  # Assume '*' matches 0 characters initially

            # 3. Mismatch occurred, but a previous '*' exists: backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1
                match_idx += 1
                s_ptr = match_idx  # Let '*' consume one more character

            # 4. Mismatch occurred and no previous '*' to backtrack to
            else:
                return False

        # Consume remaining trailing '*' characters in pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1

        # Check if the whole pattern was consumed
        return p_ptr == len(p)