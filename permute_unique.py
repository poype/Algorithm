# https://leetcode.cn/problems/permutations-ii/

from typing import List, Set


class Solution(object):
    def __init__(self):
        self.result = []
        self.unique_index = set()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.pick_number(nums, 0, [])
        return self.result

    def pick_number(self, nums: List[int], pos: int, one_list: List[int]):
        """
        给第 pos 个位置挑选数字
        unique_num_set是记录该位置已经出现过的数字，同一个位置不能使用两个相同的数字，避免重复的排列结果
        self.unique_index是用于记录被其它位置已经使用过的nums数组下标
        """
        unique_num_set = set()

        for i in range(len(nums)):
            if self.unique_index.__contains__(i):
                # nums数组中的这个元素已经被其它位置占用了
                continue

            if unique_num_set.__contains__(nums[i]):
                # 相同的数字已经在该位置被使用了
                continue

            self.unique_index.add(i)     # 占用 i 下标
            unique_num_set.add(nums[i])  # 记录当前位置已经使用过的数字值

            one_list.append(nums[i])

            if pos == len(nums) - 1:
                self.result.append(one_list[:])   # 为最后一个位置选数字，则产生一组排列结果。注意list的拷贝方式
            else:
                self.pick_number(nums, pos + 1, one_list)  # 继续给下一个位置选数字

            one_list.pop()  # 为该 位置 使用下一个数字做准备
            self.unique_index.remove(i)  # 当前位置不再占用下标i


s = Solution()
print(s.permuteUnique([1, 1, 2]))

# 这个程序有两个地方值得学习
# 1. 排列算法的实现
# 2. list 的拷贝方式 是 nums[:]， 可千万不要for-each遍历copy
