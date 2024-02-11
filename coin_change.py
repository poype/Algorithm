# https://leetcode.cn/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        return self.__coin_change__(coins, amount, 0)

    def __coin_change__(self, coins: List[int], amount: int, start: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if start == len(coins):
            return -1

        cnt1, cnt2, cnt3 = -1, -1, -1
        val1 = self.__coin_change__(coins, amount - coins[start], start)
        if val1 != -1:
            cnt1 = val1 + 1

        val2 = self.__coin_change__(coins, amount - coins[start], start + 1)
        if val2 != -1:
            cnt2 = val2 + 1

        cnt3 = self.__coin_change__(coins, amount, start + 1)

        cnt = 2 ** 32 - 1
        if cnt1 != -1:
            cnt = cnt1
        if cnt2 != -1 and cnt2 < cnt:
            cnt = cnt2
        if cnt3 != -1 and cnt3 < cnt:
            cnt = cnt3

        if cnt == 2 ** 32 - 1:
            return -1
        return cnt

s = Solution()
coins = [1]
amount = 0
print(s.coinChange(coins, amount))
