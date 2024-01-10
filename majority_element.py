# https://leetcode.cn/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def __init__(self):
        self.count_dict = {}

    def majorityElement(self, nums: List[int]) -> int:
        for num in nums:
            self.count_num(num)

        for num in self.count_dict:
            if self.count_dict[num] > len(nums) / 2:
                return num

        return -1

    def count_num(self, num):
        if num not in self.count_dict:
            self.count_dict[num] = 0

        self.count_dict[num] += 1


s = Solution()
l = [2, 2, 1, 1, 1, 2, 2]
print(s.majorityElement(l))
