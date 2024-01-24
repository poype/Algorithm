# https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)

        max_len = 0
        for num in nums:
            if (num - 1) in num_set:
                # 前数存在，num肯定不是起点，skip过
                continue

            cnt = 1
            p = num
            while (p + 1) in num_set:
                p = p + 1
                cnt += 1

            max_len = max(max_len, cnt)

        return max_len


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
s = Solution()
print(s.longestConsecutive(nums))
