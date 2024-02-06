# https://leetcode.cn/problems/combinations/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.take_num(1, n, k)

    def take_num(self, start: int, end: int, k: int) -> List[List[int]]:
        result = []
        if k == 1:
            for i in range(start, end + 1):
                result .append([i])
            return result

        for i in range(start, end - k + 2):
            part_result = self.take_num(i + 1, end, k - 1)
            for l in part_result:
                l.insert(0, i)
            result.extend(part_result)

        return result


s = Solution()
print(s.combine(4, 2))
