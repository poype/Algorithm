# https://leetcode.cn/problems/summary-ranges/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if len(nums) == 0:
            return result

        start, end = 0, 0

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                end = i
            else:
                self.append_result(start, end, nums, result)
                start, end = i, i

        self.append_result(start, end, nums, result)
        return result

    def append_result(self, start: int, end: int, nums: List[int], result: List[str]):
        if start == end:
            result.append(f"{nums[start]}")
        else:
            result.append(f"{nums[start]}->{nums[end]}")


s = Solution()
nums = [0,1,2,4,5,7]
result = s.summaryRanges(nums)
print(result)
