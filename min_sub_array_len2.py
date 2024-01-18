# https://leetcode.cn/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        start, i = 0, 0

        sum_value = 0
        min_len = 999999
        for start in range(n):
            if start > 0:
                sum_value -= nums[start - 1]
                if sum_value >= target:
                    if i - start < min_len:
                        min_len = i - start
                    continue

            while i < n:
                sum_value += nums[i]
                i += 1
                if sum_value >= target:
                    if i - start < min_len:
                        min_len = i - start
                    break

        return min_len


s = Solution()
nums = [2, 3, 1, 2, 4, 3]
target = 7
result = s.minSubArrayLen(target, nums)
print(result)


# 此题算法想清楚之后，花费了超过半个小时才成功
