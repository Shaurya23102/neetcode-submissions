class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicto = {}

        for num in nums:
            if num in dicto:
                dicto[num] += 1
            else:
                dicto[num] = 1

        freq = sorted(dicto.items(), key=lambda x: x[1], reverse=True)

        ans = []

        for i in range(k):
            ans.append(freq[i][0])

        return ans