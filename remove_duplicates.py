# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/

from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        num = nums[0]

        k = 0
        for i in range(1, len(nums)):
            if num != nums[i]:
                k += 1
                nums[k] = nums[i]
                num = nums[i]

        return k + 1


nums = [1, 1, 2]

s = Solution()

count = s.removeDuplicates(nums)
print(count)
print(nums)
