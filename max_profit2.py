# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        if n == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0

        # False 表示price往下走，True 表示price往上走
        flag = prices[1] > prices[0]
        minimum = prices[0]

        sum_profit = 0
        for i in range(2, n):
            if prices[i] > prices[i - 1]:
                if not flag:
                    # i - 1 是最低点
                    minimum = prices[i - 1]

                if i == n - 1:
                    sum_profit += (prices[i] - minimum)
                flag = True
            else:
                if flag:
                    # i - 1 是最高点
                    sum_profit += (prices[i - 1] - minimum)
                flag = False

        return sum_profit


s = Solution()
l = [1, 2, 3, 4, 5]
print(s.maxProfit(l))
