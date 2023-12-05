
from typing import List

class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # 这个排序是有必要的，可以避免[1, 2] [2, 1]这种情况出现
        return self.combination(0, candidates, target)

    def combination(self, start: int, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        unique_set = set()
        for i in range(start, len(candidates)):
            if unique_set.__contains__(candidates[i]):  # 由于有重复数据，如果某个数据已经在该层级出现过了，就不再使用第二次了
                continue
            unique_set.add(candidates[i])

            if candidates[i] == target:
                result.append([candidates[i]])
            elif candidates[i] < target:
                # 相比与combinationSum1，这里的start是下一个元素的位置
                part_result = self.combination(i + 1, candidates, target - candidates[i])
                if len(part_result) > 0:
                    for item_list in part_result:
                        item_list.append(candidates[i])
                        result.append(item_list)

        return result


s = Solution()
candidates = [2,5,2,1,2]
target = 5

print(s.combinationSum2(candidates, target))