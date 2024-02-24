# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
# 此题花了一个小时的时间，数组方面的题有必要加强

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k指向列表头部，i扫描整个列表
        k, i, n = 0, 0, len(nums)
        while i < n:
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[k] = nums[i]
                nums[k + 1] = nums[i + 1]
                i += 2
                while i < n and nums[i] == nums[k]:
                    i += 1
                k += 2
            else:
                nums[k] = nums[i]
                i += 1
                k += 1
        return k


s = Solution()
l = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(s.removeDuplicates(l))
print(l)
