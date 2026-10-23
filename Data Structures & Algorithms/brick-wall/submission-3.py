
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        a = []

        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i]) - 1):
                s += wall[i][j]
                a.append(s)

        a = sorted(a)

        max_count = 0
        count = 0
        prev = None

        for i in range(len(a)):
            if a[i] == prev:
                count += 1
            else:
                count = 1
                prev = a[i]

            max_count = max(max_count, count)

        return len(wall) - max_count
