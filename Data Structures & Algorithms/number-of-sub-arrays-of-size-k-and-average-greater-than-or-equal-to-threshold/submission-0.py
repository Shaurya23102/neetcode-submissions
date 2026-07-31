from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        for i in range(len(arr) - k + 1):
            if sum(arr[i:i+k]) / k >= threshold:
                count += 1
        return count
