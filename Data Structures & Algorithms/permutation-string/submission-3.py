class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = []
        for i in range(len(s2) - len(s1) + 1):
            a.append(s2[i:i+len(s1)])
        s = ["".join(sorted(word)) for word in a]
        target = "".join(sorted(s1))   
        for i in range(len(s)):
            if target == s[i]:
                return True
        return False
