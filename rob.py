# https://leetcode.cn/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        return self.__rob__(nums, 0, dp)

    def __rob__(self, nums: List[int], start: int, dp: list[int]) -> int:
        if dp[start] != -1:
            return dp[start]

        if start == len(nums) - 1:
            dp[start] = nums[len(nums) - 1]
            return nums[len(nums) - 1]

        if start == len(nums) - 2:
            dp[start] = max(nums[len(nums) - 1], nums[len(nums) - 2])
            return max(nums[len(nums) - 1], nums[len(nums) - 2])

        val1 = nums[start] + self.__rob__(nums, start + 2, dp)
        val2 = self.__rob__(nums, start + 1, dp)
        dp[start] = max(val1, val2)
        return max(val1, val2)


s = Solution()
l = [2, 7, 9, 3, 1]
print(s.rob(l))
