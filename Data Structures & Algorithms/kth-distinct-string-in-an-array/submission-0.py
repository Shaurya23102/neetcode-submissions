class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        
        for val in arr:
            d[val] = d.get(val, 0) + 1

        count = 0

        for val in arr:
            if d[val] == 1:
                count += 1

                if count == k:
                    return val

        return ""