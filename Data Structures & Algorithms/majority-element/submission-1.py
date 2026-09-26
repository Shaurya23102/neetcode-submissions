class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        return d[0][0]

        