# https://leetcode.cn/problems/4sum/


from typing import List

class Solution(object):
    def fourSum(self, nums:List[int], target: int) -> List[List[int]]:
        return self.nSum(nums, 4, target, 0)

    def nSum(self, nums: List[int], count: int, sum: int, start_index: int) -> List[list[int]]:
        result = []

        if count == 1:
            for i in range(start_index, len(nums)):
                if nums[i] == sum:
                    result.append([nums[i]])
                    return result
        else:
            # 增加set过滤掉已经计算过的值
            unique_set = set()
            for i in range(start_index, len(nums)):
                if unique_set.__contains__(nums[i]):
                    continue
                unique_set.add(nums[i])

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

s = Solution()
l = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
target = 200

print(s.fourSum(l, target))