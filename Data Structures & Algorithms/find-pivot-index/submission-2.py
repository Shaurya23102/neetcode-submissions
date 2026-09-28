class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s1 = sum(nums[0:i])
            s2 = sum(nums[i+1:])
            if s1 == s2:
                return i

        return -1