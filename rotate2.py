# https://leetcode.cn/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        for i in range(k):
            self.move_right(nums)

    def move_right(self, nums: List[int]):
        last_element = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = last_element


s = Solution()
l = [1, 2, 3, 4, 5, 6, 7]
s.rotate(l, 3)
print(l)
