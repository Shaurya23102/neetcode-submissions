class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        t = temperatures[:]

        for i in range(len(t)):
            days = 0
            for j in range(i + 1, len(t)):
                if t[j] > t[i]:
                    days = j - i
                    break
            result.append(days)
        
        return result