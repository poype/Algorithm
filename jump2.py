# https://leetcode.cn/problems/jump-game-ii/

from typing import List

class Solution(object):
    def __init__(self):
        self.flags = []

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        self.flags = [-1 for i in range(len(nums))]

        return self.jump_from_start(nums, 0)

    def jump_from_start(self, nums: List[int], start: int) -> int:
        if self.flags[start] > 0:
            return self.flags[start]

        if nums[start] >= len(nums) - start - 1:
            self.flags[start] = 1
            return 1

        if nums[start] == 0:
            self.flags[start] = 2 ** 32 - 2
            return 2 ** 32 - 2

        min_steps = 2 ** 32 - 2

        for i in range(1, nums[start] + 1):
            steps = self.jump_from_start(nums, start + i)
            if steps < min_steps:
                min_steps = steps

        self.flags[start] = min_steps + 1
        return min_steps + 1

s = Solution()
print(s.jump([2,3,0,1,4]))
