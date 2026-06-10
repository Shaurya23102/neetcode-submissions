class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(numbers):
            goal = target - num

            if goal in d:
                a = [d[goal] + 1, i + 1]
                break

            d[num] = i

        return a