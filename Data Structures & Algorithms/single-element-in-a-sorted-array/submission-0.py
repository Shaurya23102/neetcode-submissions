class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        for val in nums:
            d[val] = d.get(val, 0) + 1
        
        return (min(d, key=d.get))