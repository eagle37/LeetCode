# Last updated: 8/27/2026, 3:01:09 PM
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in target:
            freq[ch] = freq.get(ch, 0) - 1

        for i in range(n - 1, -1, -1):

            freq[target[i]] += 1

            if any(x < 0 for x in freq.values()):
                continue

            candidates = [
                ch for ch in freq
                if freq[ch] > 0 and ch > target[i]
            ]

            if not candidates:
                continue

            ch = min(candidates)
            freq[ch] -= 1
            suffix = []

            for c in sorted(freq):
                suffix.append(c * freq[c])

            return target[:i] + ch + ''.join(suffix)

        return ""