class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        res = 0
        freq = {}

        for R in range(len(s)):
            freq[s[R]] = freq.get(s[R], 0) + 1
            while (R - L + 1) - max(freq.values()) > k:
                freq[s[L]] -= 1
                L += 1

            res = max(res, R - L + 1)

        return res
