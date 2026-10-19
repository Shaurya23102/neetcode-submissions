class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish = 0
        wait_times = []

        for arrival, service in customers:
            start = max(finish, arrival)
            finish = start + service

            wait_times.append(finish - arrival)

        return sum(wait_times)/len(wait_times)
