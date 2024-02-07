# https://leetcode.cn/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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

        return max_val


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
print(s.maxSubArray(nums))
