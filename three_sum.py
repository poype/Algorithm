# https://leetcode.cn/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.nSum(nums, 3, 0, 0)

    def nSum(self, nums: List[int], count: int, result: int, start_index: int) -> List[list[int]]:
        current_l = []

        if count == 1:
            for i in range(start_index, len(nums)):
                if nums[i] == result:
                    current_l.append([nums[i]])
        else:
            for i in range(start_index, len(nums)):
                next_l = self.nSum(nums, count - 1, result - nums[i], i + 1)
                if len(next_l) > 0:
                    for k in range(len(next_l)):
                        next_l[k].insert(0, nums[i])
                        current_l.append(next_l[k])

        return current_l


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
