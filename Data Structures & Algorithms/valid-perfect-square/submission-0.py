class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num ** 0.5)   # take integer square root
        return root * root == num
