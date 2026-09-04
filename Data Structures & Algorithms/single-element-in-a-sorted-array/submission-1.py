class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid % 2 == 1:
                mid -= 1              # force mid to be even
            if nums[mid] == nums[mid + 1]:
                l = mid + 2           # pair intact, single element is further right
            else:
                r = mid               # pair broken, single element is here or to the left
        return nums[l]
