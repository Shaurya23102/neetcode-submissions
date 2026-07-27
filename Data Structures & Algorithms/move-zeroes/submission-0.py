class Solution:
    def moveZeroes(self, nums: List[int]) -> None:


        l = 0
        n = len(nums)
        count = 0

        while count < n:
            if nums[l] == 0:
                nums.pop(l)
                nums.append(0)
            else:
                l += 1
            count += 1

