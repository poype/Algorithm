# https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_highest_list = [0]
        right_highest_list = [0]

        left_highest = 0
        right_highest = 0

        for i in range(1, n):
            if height[i - 1] > left_highest:
                left_highest = height[i - 1]
            left_highest_list.append(left_highest)

        for i in range(n - 2, -1, -1):
            if height[i + 1] > right_highest:
                right_highest = height[i + 1]
            right_highest_list.insert(0, right_highest)

        sum_value = 0
        for i in range(n):
            if min(left_highest_list[i], right_highest_list[i]) > height[i]:
                sum_value += min(left_highest_list[i], right_highest_list[i]) - height[i]

        return sum_value


s = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(s.trap(height))
