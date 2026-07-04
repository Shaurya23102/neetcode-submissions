class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for n in nums:
            if target in nums:
                return True
            else:
                return False
        