from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        zero_count = nums.count(0)

        if zero_count > 1:
            return [0] * len(nums)

        product = 1
        for num in nums:
            if num != 0:
                product *= num

        ans = []

        for num in nums:
            if zero_count == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // num)

        return ans