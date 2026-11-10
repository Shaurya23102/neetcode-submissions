class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i,j = 0,1
        n = nums[:]
        while j <= len(nums)-1:
            if nums[i]==nums[j]:
                nums[i]= nums[i]*2
                nums[j]= 0
                i+=2
                j+=2
            else:
                i+=1
                j+=1
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        while k < len(nums):
            nums[k] = 0
            k += 1
        return nums
        
