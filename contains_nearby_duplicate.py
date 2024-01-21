# https://leetcode.cn/problems/contains-duplicate-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_pos_map = {}

        for i in range(len(nums)):
            if nums[i] not in num_pos_map:
                num_pos_map[nums[i]] = []
            num_pos_map[nums[i]].append(i)

        for key in num_pos_map.keys():
            if len(num_pos_map[key]) >= 2:
                pos_list = num_pos_map[key]
                for i in range(1, len(pos_list)):
                    if abs(pos_list[i] - pos_list[i - 1]) <= k:
                        return True

        return False

s = Solution()
nums = [1,2,3,1]
k = 3
print(s.containsNearbyDuplicate(nums, k))