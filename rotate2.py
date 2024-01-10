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

        n = len(nums)
        left_slice = nums[0: n - k]

        # 直接将后k个元素copy到数组前部
        for i in range(k):
            nums[i] = nums[n - k + i]

        for i in range(k, n):
            nums[i] = left_slice[i - k]

    # 下面这个方法无用了
    def move_right(self, nums: List[int]):
        last_element = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = last_element


s = Solution()
l = [1, 2, 3, 4, 5, 6, 7]
s.rotate(l, 3)
print(l)
