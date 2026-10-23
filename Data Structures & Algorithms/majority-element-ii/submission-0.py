from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        d = Counter(nums)

        a = [num for num, freq in d.items() if freq > len(nums) // 3]

        return a
        
        