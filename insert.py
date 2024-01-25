# https://leetcode.cn/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        if len(intervals) == 0:
            stack.append(newInterval)
            return stack

        start, end = newInterval[0], newInterval[1]
        i = 0
        while i < len(intervals):
            if newInterval[0] <= intervals[i][0]:
                break
            stack.append(intervals[i])
            i += 1

        if i > 0 and newInterval[0] <= intervals[i - 1][1]:
            stack.pop()
            i -= 1  # 既然pop出一个item，那i也要减1
            start = intervals[i][0]

        if i == len(intervals):  # 已经到了最后一个item
            end = max(intervals[i - 1][1], newInterval[1])
            stack.append([start, end])
            return stack

        while i < len(intervals):
            if newInterval[1] <= intervals[i][1]:
                break
            i += 1

        if i < len(intervals) and newInterval[1] >= intervals[i][0]:
            end = intervals[i][1]
            i += 1

        stack.append([start, end])

        while i < len(intervals):
            stack.append(intervals[i])
            i += 1

        return stack


s = Solution()
intervals = [[0,5],[8,9]]
newInterval = [3,4]
print(s.insert(intervals, newInterval))
