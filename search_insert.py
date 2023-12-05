
from typing import List

class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return left
# 当target不存在时，只需返回left的值即可
# 因为如果没找到target，执行到最后left > right退出while循环，则从left开始往后的所有元素都大于target，从right开始往前的所有元素都小于target
# 而target的插入点就应该是第一个大于它的元素
# 有两个边界case： 1. left == len(s)  2. right == -1，但仍然满足使用left值


s = Solution()
nums = [3,4,5,6]
target = 2

result = s.searchInsert(nums, target)
print(result)



