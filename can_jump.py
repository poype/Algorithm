# https://leetcode.cn/problems/jump-game/

from typing import List


class Solution(object):
    def __init__(self):
        self.flags = []

    def canJump(self, nums: List[int]) -> bool:
        self.flags = [None for i in range(len(nums))]

        return self.can_jump_from_start(nums, 0)

    def can_jump_from_start(self, nums: List[int], start: int) -> bool:
        if self.flags[start] is not None:
            return self.flags[start]

        if start == len(nums) - 1:
            self.flags[start] = True
            return True

        if nums[start] >= len(nums) - start - 1:
            self.flags[start] = True
            return True

        if nums[start] <= 0:
            self.flags[start] = False
            return False

        for i in range(1, nums[start] + 1):
            if self.can_jump_from_start(nums, start + i):
                self.flags[start] = True
                return True

        self.flags[start] = False
        return False

s = Solution()
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))