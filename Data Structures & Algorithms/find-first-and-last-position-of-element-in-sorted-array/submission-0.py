class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = 0, len(nums) - 1
        a = [-1, -1]                      # default when target is not found
        d = Counter(nums)

        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                start = m
                while start > 0 and nums[start - 1] == target:
                    start -= 1            # walk left to the first occurrence
                a = [start, start + d[target] - 1]
                break
            elif target > nums[m]:        # fixed: compare with the value, not the index
                l = m + 1
            else:
                h = m - 1
        return a
        