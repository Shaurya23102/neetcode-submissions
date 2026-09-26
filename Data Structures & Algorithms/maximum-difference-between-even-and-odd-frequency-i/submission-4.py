class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        odd = []
        even = []

        for f in freq.values():
            if f % 2:
                odd.append(f)
            else:
                even.append(f)

        return max(odd) - min(even)