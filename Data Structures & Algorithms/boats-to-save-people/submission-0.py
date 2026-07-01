class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        w = people[:]
        w.sort()
        times = 0

        while len(w) > 0:
            if len(w) == 1:
                times += 1
                w.pop()
            elif w[0] + w[-1] <= limit:
                times += 1
                w.pop(-1)
                w.pop(0)
            else:
                times += 1
                w.pop(-1)

        return times
