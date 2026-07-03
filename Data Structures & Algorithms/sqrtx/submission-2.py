class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1000000000):
            if i * i == x:
                return i
                break
            elif i * i > x:
                return i - 1
                break
