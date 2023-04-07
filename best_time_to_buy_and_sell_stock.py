from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_profit = 0

        while end < len(prices):
            if prices[start] < prices[end]:
                profit = prices[end] - prices[start]
                if profit > max_profit:
                    max_profit = profit
            else:
                start = end
            end += 1
        return max_profit


s = Solution()
print(s.maxProfit([7,5,2,3,1,4]))
