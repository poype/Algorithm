# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self):
        self.minimum = None

    def findMin(self, nums: List[int]) -> int:
        self.minimum = min(nums[0], nums[len(nums) - 1])
        self.__binary_search__(0, len(nums) - 1, nums)
        return self.minimum

    def __binary_search__(self, start: int, end: int, nums: List[int]):
        mid = (start + end) // 2

        if len(nums) - 1 > mid > 0 and nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1]:
            self.minimum = nums[mid]
            return

        if mid < end:
            self.__binary_search__(mid + 1, end, nums)
        if mid > start:
            self.__binary_search__(start, mid - 1, nums)


s = Solution()
nums = [11, 13, 15, 17]

print(s.findMin(nums))
