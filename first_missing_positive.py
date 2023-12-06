# https://leetcode.cn/problems/first-missing-positive/description/

from typing import List

class Solution(object):
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:    # 这里要使用while，不能用if
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # 这行代码nums[nums[i] - 1], nums[i]的顺序是不能变的
                # 一定要确保nums[nums[i] - 1]在nums[i]的前面，即要先修改nums[nums[i] - 1]的值，再修改nums[i]的值

        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1

        return n + 1


s = Solution()

print(s.firstMissingPositive([1,2,0]))
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7,8,9,11,12]))
