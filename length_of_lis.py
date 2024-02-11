# https://leetcode.cn/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self):
        self.max_length = 1

    def lengthOfLIS(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            self.__lis__(nums, i, [])

        return self.max_length

    def __lis__(self, nums: List[int], start: int, lis: List[int]):
        lis.append(nums[start])
        if len(lis) > self.max_length:
            self.max_length = len(lis)

        for i in range(start + 1, len(nums)):
            if nums[start] < nums[i]:
                self.__lis__(nums, i, lis)

        lis.pop()


s = Solution()
nums = [7, 7, 7, 7, 7, 7, 7]
print(s.lengthOfLIS(nums))
