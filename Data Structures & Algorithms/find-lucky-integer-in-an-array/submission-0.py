from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        res = -1
        for num, freq in c.items():
            if num == freq:
                res = max(res, num)
        return res
