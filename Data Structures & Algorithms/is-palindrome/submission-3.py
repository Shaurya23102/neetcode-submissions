class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(ch for ch in s if ch.isalnum())
        words = result.split()
        ss1 = ''.join(words)
        ss1 = ss1.lower()
        ss = ss1[::-1]

        bools = False
        if ss1 == ss:
            bools =  True 
        else:
            bools = False      

        return bools