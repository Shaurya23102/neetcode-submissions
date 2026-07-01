class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = max(len(word1), len(word2))
        final = []

        for i in range(a):
            if i < len(word1):
                final.append(word1[i])
            if i < len(word2):
                final.append(word2[i])

        final = ("".join(final))
        return final
