import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # Get the two largest stones
            a, b = heapq.nlargest(2, stones)
            stones.remove(a)
            stones.remove(b)

            # If they are not equal, push the difference back
            if a != b:
                stones.append(a - b)

        # Return the last stone or 0 if none remain
        return stones[0] if stones else 0
