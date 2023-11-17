# https://leetcode.cn/problems/remove-element/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] != val:
                i += 1
                continue

            if nums[j] == val:
                j -= 1
                continue

            nums[i], nums[j] = nums[j], nums[i]

        if nums[i] == val:
            return i

        return i + 1