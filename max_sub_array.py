# https://leetcode.cn/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max = nums[0], nums[0]

        for i in range(1, len(nums)):
            if sum + nums[i] > nums[i]:
                sum = sum + nums[i]
            else:
                sum = nums[i]

            if sum > max:
                max = sum

        return max


s = Solution()
print(s.maxSubArray([1]))
