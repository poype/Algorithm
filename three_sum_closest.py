# https://leetcode.cn/problems/3sum-closest/

from typing import List


# 如果按照最一般的解法，就是把数组中所有3个元素组合的和都求出来，需要时间复杂度为O(n3)。
# 下面的解法只需要O(n2)的时间复杂度

class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = 2 ** 31 - 1
        nums.sort()
        result = None

        for i in range(len(nums) - 2):
            o, p, q = i, i + 1, len(nums) - 1
            while p < q:
                sum = nums[o] + nums[p] + nums[q]
                if abs(sum - target) < min_diff:
                    min_diff = abs(sum - target)
                    result = sum

                # 如果sum已经大于target，由于数组是有序的，再继续增大值是没必要的，所有数组最后一个元素向前移动
                if sum > target:
                    q -= 1

                # 如果sum小于target，则可以继续增大数组中的值，所以p++，但o保持不变。
                if sum < target:
                    p += 1

                if sum == target:
                    return sum

        return result


s = Solution()
l = [1, 1, 1, 0]

print(s.threeSumClosest(l, -100))
