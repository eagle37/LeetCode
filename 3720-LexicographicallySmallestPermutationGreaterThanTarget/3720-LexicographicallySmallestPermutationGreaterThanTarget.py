# Last updated: 8/27/2026, 3:00:33 PM
1class Solution:
2    def lexGreaterPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4        freq = {}
5
6        for ch in s:
7            freq[ch] = freq.get(ch, 0) + 1
8
9        for ch in target:
10            freq[ch] = freq.get(ch, 0) - 1
11
12        for i in range(n - 1, -1, -1):
13
14            freq[target[i]] += 1
15
16            if any(x < 0 for x in freq.values()):
17                continue
18
19            candidates = [
20                ch for ch in freq
21                if freq[ch] > 0 and ch > target[i]
22            ]
23
24            if not candidates:
25                continue
26
27            ch = min(candidates)
28            freq[ch] -= 1
29            suffix = []
30
31            for c in sorted(freq):
32                suffix.append(c * freq[c])
33
34            return target[:i] + ch + ''.join(suffix)
35
36        return ""