# https://leetcode.cn/problems/combination-sum/description/

from typing import List


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combination(0, candidates, target)

    # 如果没有这个start参数，那就变成排列了，会出现[3, 5]和[5, 3]这种重复数据
    # 为了计算组合，必须让计算向一个方向迭代，不能往会迭代，所以加了start这个参数

    def combination(self, start: int, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for i in range(start, len(candidates)):
            if candidates[i] == target:
                result.append([candidates[i]])
            elif candidates[i] < target:
                part_result = self.combination(i, candidates, target - candidates[i])
                if len(part_result) > 0:
                    for item_list in part_result:
                        item_list.append(candidates[i])
                        result.append(item_list)

        return result


s = Solution()
candidates = [2, 3, 5]
target = 8

print(s.combinationSum(candidates, target))
