# https://leetcode.cn/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        n = len(nums)
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        for k in range(n):  # 记住动态规划斜线如何走
            i, j = 0, k
            while i < n - k:
                if i == j:
                    matrix[i][j] = nums[i]
                elif i + 1 == j:
                    matrix[i][j] = nums[i] + nums[j]
                else:
                    matrix[i][j] = matrix[i+1][j-1] + nums[i] + nums[j]

                i += 1
                j += 1

        min_len = 9999
        for i in range(n):
            for j in range(n):
                if matrix[i][j] >= target and j - i + 1 < min_len:
                    min_len = j - i + 1

        return min_len


s = Solution()
nums = [1,1,1,1,1,1,1,1]
target = 11
result = s.minSubArrayLen(target, nums)
print(result)


