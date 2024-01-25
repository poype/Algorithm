# https://leetcode.cn/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])  # 注意这个排序方式

        stack = []
        stack.append(intervals[0])
        for i in range(1, len(intervals)):
            peek = stack[len(stack) - 1]

            if intervals[i][0] > peek[1]:
                stack.append(intervals[i])
            else:
                stack.pop()
                new_internal = [peek[0], max(peek[1], intervals[i][1])]
                stack.append(new_internal)

        return stack


s = Solution()
intervals = [[1,4],[4,5]]
result = s.merge(intervals)
print(result)
