# https://leetcode.cn/problems/maximum-sum-circular-subarray/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [[0 for _ in range(m)] for _ in range(m)]
        max_val = nums[0]

        for k in range(m):
            i, j = 0, k
            while i < m - k:
                if i == j:
                    dp[i][j] = nums[i]
                elif j - 1 == i:
                    dp[i][j] = nums[i] + nums[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] + nums[i] + nums[j]

                if dp[i][j] > max_val:
                    max_val = dp[i][j]
                i += 1
                j += 1

        whole_sum = sum(nums)
        for k in range(1, m):
            i, j = k, 0
            while i < m:
                if i - 1 == j:
                    dp[i][j] = whole_sum
                else:
                    dp[i][j] = whole_sum - dp[j + 1][i - 1]
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
                i += 1
                j += 1

        return max_val


s = Solution()
nums1 = [5,-3,5]
nums2 = [1,-2,3,-2]
nums3 = [3,-2,2,-3]
nums = [-2]

print(s.maxSubarraySumCircular(nums))
