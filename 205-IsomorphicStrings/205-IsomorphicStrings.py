# Last updated: 8/15/2026, 4:31:51 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st, map_ts = {}, {}

        for i in range(len(s)):
            cs, ct = s[i], t[i]

            if (cs in map_st and map_st[cs] != ct) or (ct in map_ts and map_ts[ct] != cs):
                return False

            map_st[cs] = ct
            map_ts[ct] = cs

        return True