class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #ss,rr = s.split(),t.split()
        bool = False
        if sorted(s) == sorted(t):
            bool = True
        else:
            bool = False

        return bool 
        
        