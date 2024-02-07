# https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        whole_sum = sum(nums)
        max_sum = whole_sum
        total_cnt = len(nums)

        if total_cnt == 1:
            return max_sum

        cnt = 1
        loop_cnt = total_cnt // 2
        if total_cnt % 2 == 1:
            loop_cnt += 1

        while cnt <= loop_cnt:
            i = 0
            while i <= total_cnt - cnt:
                sum_val = sum(nums[i: i + cnt])
                if sum_val > max_sum:
                    max_sum = sum_val

                if whole_sum - sum_val > max_sum:
                    max_sum = whole_sum - sum_val

                i += 1

            cnt += 1

        return max_sum


s = Solution()
nums1 = [5,-3,5]
nums2 = [1,-2,3,-2]
nums3 = [3,-2,2,-3]
nums = [-2]

print(s.maxSubarraySumCircular(nums))
