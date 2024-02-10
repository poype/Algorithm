# https://leetcode.cn/problems/find-peak-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.__binary_search__(0, len(nums) - 1, nums)

    def __binary_search__(self, start, end, nums) -> int:
        mid = (start + end) // 2
        if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            return self.__binary_search__(mid + 1, end, nums)

        if mid > 0 and nums[mid] < nums[mid - 1]:
            return self.__binary_search__(start, mid - 1, nums)

        return mid


s = Solution()
nums = [1,2,3,1]
print(s.findPeakElement(nums))
