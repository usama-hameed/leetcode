from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        start = 0
        end = 2
        total_cost = 0
        while start < len(cost):
            total_cost += sum(cost[start:end])
            start += 3
            end = start + 2
        return total_cost


s = Solution()
print(s.minimumCost([5,5]))
