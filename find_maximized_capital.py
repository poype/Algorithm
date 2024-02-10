# https://leetcode.cn/problems/ipo/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import heapq


class Project:
    def __init__(self, profit: int, capital: int, idx: int):
        self.pure_profit = profit - capital
        self.capital = capital
        self.profit = profit
        self.idx = idx

    def __lt__(self, other: 'Project'):
        return self.profit > other.profit


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        total_earn = 0
        for _ in range(k):
            heap_queue = []

            for i in range(len(profits)):
                heapq.heappush(heap_queue, Project(profits[i], capital[i], i))

            while len(heap_queue) > 0:
                project = heapq.heappop(heap_queue)
                if w >= project.capital:
                    w += project.pure_profit
                    total_earn += profits[project.idx]
                    profits.pop(project.idx)
                    capital.pop(project.idx)
                    break
        return total_earn


s = Solution()
k = 2
w = 2
profits = [1, 2, 3]
capital = [1, 1, 2]
print(s.findMaximizedCapital(k, w, profits, capital))
