from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        for val in nums:
            d[val] = d.get(val, 0) + 1

        a = []
        n = len(nums)

        for i in range(1, n+1):   # check numbers from 1 to n
            if i not in d:        # if number is missing
                a.append(i)

        return a
