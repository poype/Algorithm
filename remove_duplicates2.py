# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
# 此题花了一个小时的时间，数组方面的题有必要加强

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i = 0, 1

        while i < len(nums):
            # 如果只剩最后一个元素，或者不是两个连续相等的元素
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                nums[k + 1] = nums[i]
                k += 1
                i += 1
                continue

            # 两个或两个以上连续相等的元素
            i += 1

            if nums[i] != nums[k]:
                nums[k + 1] = nums[i - 1]
                nums[k + 2] = nums[i]
                k += 2
            else:
                nums[k + 1] = nums[i - 1]
                k += 1

            i += 1

            # 两个以上连续相同的元素，后面相同的元素直接跳过
            while i < len(nums) and nums[i] == nums[k]:
                i += 1

        return k + 1


s = Solution()
l = [1,2,2,2]
print(s.removeDuplicates(l))
print(l)
