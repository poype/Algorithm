# https://leetcode.cn/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas):
            pos = self.move_farthest_pos(i, gas, cost)
            if pos == i:
                return i

            if pos > i:
                i = pos
            else:
                return -1  # 这已经能够缺点找不到结果了

        return -1

    def move_farthest_pos(self, start_index: int, gas: List[int], cost: List[int]) -> int:
        """
        从start_index开始，可以走到最远的位置
        :return: 可以走到最远的位置， 下一次会直接从这个点向后搜索
        """
        n = len(gas)

        i = start_index
        gas_volume = gas[i]
        if gas_volume < cost[i]:
            return start_index + 1

        gas_volume -= cost[i]
        i = (i + 1) % n

        while i != start_index:
            gas_volume += gas[i]
            if gas_volume < cost[i]:
                return i
            gas_volume -= cost[i]
            i = (i + 1) % n
        return start_index


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
gas = [2, 3, 4]
cost = [3, 4, 3]

print(s.canCompleteCircuit(gas, cost))
