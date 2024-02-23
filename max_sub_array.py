# https://leetcode.cn/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_val, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if sum_val + nums[i] > nums[i]:
                sum_val += nums[i]
            else:
                sum_val = nums[i]

            if max_sum < sum_val:
                max_sum = sum_val
        return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(nums))
