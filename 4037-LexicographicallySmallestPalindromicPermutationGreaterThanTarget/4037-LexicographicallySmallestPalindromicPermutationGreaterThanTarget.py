# Last updated: 9/4/2026, 3:23:04 PM
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        if sum(x % 2 for x in freq) > 1:
            return ""

        mid = next((i for i, x in enumerate(freq) if x % 2), None)

        for i in range(26):
            freq[i] //= 2

        ans = list(s)
        half = n // 2

        def make_palindrome():
            if mid is not None:
                ans[half] = chr(97 + mid)

            for i in range(half):
                ans[n - 1 - i] = ans[i]

        pos = 0

        while pos < half:
            x = ord(target[pos]) - 97

            if freq[x] == 0:
                break

            ans[pos] = target[pos]
            freq[x] -= 1
            pos += 1

        if pos == half:
            make_palindrome()

            result = ''.join(ans)

            if result > target:
                return result

        while True:
            if pos < half:
                start = ord(target[pos]) - 97 + 1

                for ch in range(start, 26):
                    if freq[ch] == 0:
                        continue

                    ans[pos] = chr(97 + ch)
                    freq[ch] -= 1

                    idx = pos + 1

                    for c in range(26):
                        for _ in range(freq[c]):
                            ans[idx] = chr(97 + c)
                            idx += 1

                    make_palindrome()

                    return ''.join(ans)

            if pos == 0:
                return ""

            pos -= 1
            freq[ord(target[pos]) - 97] += 1