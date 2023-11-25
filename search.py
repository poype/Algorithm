# https://leetcode.cn/problems/search-in-rotated-sorted-array/

from typing import List


class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        split_point = self.split_index(nums, 1, len(nums) - 1, nums[0])
        index = self.binary_search(nums, target, split_point, len(nums) - 1)
        if index == -1:
            index = self.binary_search(nums, target, 0, split_point - 1)
        return index

    def split_index(self, nums: List[int], left: int, right: int, first: int) -> int:
        if left < right:
            mid = (left + right) // 2
            if first < nums[mid]:
                return self.split_index(nums, mid + 1, right, first)
            else:
                return self.split_index(nums, left, mid - 1, first)

        if left == len(nums) - 1 or right == len(nums) - 1:
            return len(nums) - 1

        if nums[left] <= nums[left + 1]:
            return left
        else:
            return left + 1

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if target < nums[mid]:
                return self.binary_search(nums, target, left, mid - 1)
            else:
                return self.binary_search(nums, target, left + 1, right)

        return -1
