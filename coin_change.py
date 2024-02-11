# https://leetcode.cn/problems/coin-change/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[None for _ in range(len(coins))] for _ in range(amount + 1)]
        return self.__coin_change__(coins, amount, 0, cache)

    def __coin_change__(self, coins: List[int], amount: int, start: int, cache: List[List[Optional[int]]]) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if start == len(coins):
            return -1

        if cache[amount][start] is not None:
            return cache[amount][start]

        cnt1, cnt2, cnt3 = -1, -1, -1
        val1 = self.__coin_change__(coins, amount - coins[start], start, cache)
        if val1 != -1:
            cnt1 = val1 + 1

        val2 = self.__coin_change__(coins, amount - coins[start], start + 1, cache)
        if val2 != -1:
            cnt2 = val2 + 1

        cnt3 = self.__coin_change__(coins, amount, start + 1, cache)

        cnt = 2 ** 32 - 1
        if cnt1 != -1:
            cnt = cnt1
        if cnt2 != -1 and cnt2 < cnt:
            cnt = cnt2
        if cnt3 != -1 and cnt3 < cnt:
            cnt = cnt3

        if cnt == 2 ** 32 - 1:
            cache[amount][start] = -1
            return -1
        cache[amount][start] = cnt
        return cnt


s = Solution()
coins = [1, 2, 5]
amount = 11
print(s.coinChange(coins, amount))
