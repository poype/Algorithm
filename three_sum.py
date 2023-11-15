# https://leetcode.cn/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.nSum(nums, 3, 0, 0)

    def nSum(self, nums: List[int], count: int, sum: int, start_index: int) -> List[list[int]]:
        result = []

        if count == 1:
            for i in range(start_index, len(nums)):
                if nums[i] == sum:
                    result.append([nums[i]])
        else:
            for i in range(start_index, len(nums)):
                part_result = self.nSum(nums, count - 1, sum - nums[i], i + 1)
                if len(part_result) > 0:
                    for k in range(len(part_result)):
                        part_result[k].insert(0, nums[i])
                        result.append(part_result[k])

        return self.distinct_result(result)

    def distinct_result(self, result: List[List[int]]) -> List[List[int]]:
        unique = set()
        final_result = []

        for i in range(len(result)):
            result[i].sort()
            hash_code = self.hash_list(result[i])
            if unique.__contains__(hash_code):
                continue

            unique.add(hash_code)
            final_result.append(result[i])
        return final_result

    def hash_list(self, l):
        s = ""
        for i in range(len(l)):
            s = s + str(i) + str(l[i])  # 把list中的元素和其index拼成一个字符串
        return hash(s)


nums = [-1, 0, 1, 2, -1, -4]

s = Solution()
print(s.threeSum(nums))
