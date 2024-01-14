# https://leetcode.cn/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            if self.can_complete_from_start(i, gas, cost):
                return i

        return -1

    def can_complete_from_start(self, start_index: int, gas: List[int], cost: List[int]) -> bool:
        n = len(gas)

        i = start_index
        gas_volume = gas[i]
        if gas_volume < cost[i]:
            return False

        gas_volume -= cost[i]
        i = (i + 1) % n

        while i != start_index:
            gas_volume += gas[i]
            if gas_volume < cost[i]:
                return False
            gas_volume -= cost[i]
            i = (i + 1) % n
        return True


s = Solution()
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

print(s.canCompleteCircuit(gas, cost))
