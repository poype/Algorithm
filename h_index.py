# https://leetcode.cn/problems/h-index/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        if n % 2 == 0:
            return min(citations[n // 2 - 1], n)
        else:
            return min(citations[n // 2], n)


s = Solution()
l = [1, 2]
print(s.hIndex(l))

# 此题每搞清楚题意
