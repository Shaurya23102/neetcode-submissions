class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a = []
        for i in range(len(arr)):
            a.append(abs(x - arr[i]))

        f = []

        for _ in range(k):
            m = min(a)
            idx = a.index(m)
            f.append(arr[idx])
            a[idx] = float("inf")

        f.sort()
        return f
