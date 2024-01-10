# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        minimal = prices[0]

        for i in range(1, n):
            profit = prices[i] - minimal

            if profit > max_profit:
                max_profit = profit

            if minimal > prices[i]:
                minimal = prices[i]

        return max_profit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices))

# 121. 买卖股票的最佳时机