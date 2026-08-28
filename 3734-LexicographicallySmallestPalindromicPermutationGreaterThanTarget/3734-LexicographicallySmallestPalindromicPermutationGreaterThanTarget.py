# Last updated: 8/28/2026, 9:51:06 PM
1class Solution:
2    def lexPalindromicPermutation(self, s: str, target: str) -> str:
3        n = len(s)
4        freq = [0] * 26
5
6        for ch in s:
7            freq[ord(ch) - 97] += 1
8
9        if sum(x % 2 for x in freq) > 1:
10            return ""
11
12        mid = next((i for i, x in enumerate(freq) if x % 2), None)
13
14        for i in range(26):
15            freq[i] //= 2
16
17        ans = list(s)
18        half = n // 2
19
20        def make_palindrome():
21            if mid is not None:
22                ans[half] = chr(97 + mid)
23
24            for i in range(half):
25                ans[n - 1 - i] = ans[i]
26
27        pos = 0
28
29        while pos < half:
30            x = ord(target[pos]) - 97
31
32            if freq[x] == 0:
33                break
34
35            ans[pos] = target[pos]
36            freq[x] -= 1
37            pos += 1
38
39        if pos == half:
40            make_palindrome()
41
42            result = ''.join(ans)
43
44            if result > target:
45                return result
46
47        while True:
48            if pos < half:
49                start = ord(target[pos]) - 97 + 1
50
51                for ch in range(start, 26):
52                    if freq[ch] == 0:
53                        continue
54
55                    ans[pos] = chr(97 + ch)
56                    freq[ch] -= 1
57
58                    idx = pos + 1
59
60                    for c in range(26):
61                        for _ in range(freq[c]):
62                            ans[idx] = chr(97 + c)
63                            idx += 1
64
65                    make_palindrome()
66
67                    return ''.join(ans)
68
69            if pos == 0:
70                return ""
71
72            pos -= 1
73            freq[ord(target[pos]) - 97] += 1