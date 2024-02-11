# https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [None for _ in range(len(nums))]

        max_length = 1
        for i in range(len(nums)):
            val = self.__lis__(nums, i, cache)
            if max_length < val:
                max_length = val

        return max_length

    def __lis__(self, nums: List[int], start: int, cache: List[Optional[int]]) -> int:
        if start == len(nums) - 1:
            return 1

        if cache[start] is not None:
            return cache[start]

        max_length = 0
        for i in range(start + 1, len(nums)):
            if nums[start] < nums[i]:
                length = self.__lis__(nums, i, cache)
                if max_length < length:
                    max_length = length

        cache[start] = max_length + 1
        return max_length + 1


s = Solution()
nums = [0, 1, 0, 3, 2, 3]
print(s.lengthOfLIS(nums))
