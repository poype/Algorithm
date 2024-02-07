# https://leetcode.cn/problems/permutations/

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.__permute_from_start_(nums, 0)

    def __permute_from_start_(self, nums: List[int], start: int) -> List[List[int]]:
        result = []

        if start == len(nums) - 1:
            result.append([nums[start]])
            return result

        part_result = self.__permute_from_start_(nums, start + 1)
        for num_list in part_result:
            for i in range(len(num_list) + 1):
                new_num_list = num_list[:]
                new_num_list.insert(i, nums[start])
                result.append(new_num_list)

        return result

    def permute_from_start(self, nums: List[int], start: int) -> List[List[int]]:
        result = []

        if start == len(nums) - 1:
            result.append([nums[start]])
            return result

        part_result = self.permute_from_start(nums, start + 1)
        for num_list in part_result:
            new_lists = self.insert_num_to_list(nums[start], num_list)
            for new_list in new_lists:
                result.append(new_list)

        return result

    def insert_num_to_list(self, num: int, num_list: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(num_list) + 1):
            new_list = self.copy_list(num_list)
            new_list.insert(i, num)
            result.append(new_list)
        return result

    def copy_list(self, num_list: List[int]) -> List[int]:
        new_list = []
        for num in num_list:
            new_list.append(num)
        return new_list


s = Solution()
print(s.permute([1, 0, 2]))
