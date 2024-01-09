# https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start_index = 0
        for i in range(n):
            start_index = self.insert(start_index, nums1, nums2[i], m + i) + 1

    def insert(self, start: int, nums1: List[int], target_num: int, merged_count: int) -> int:
        """
        :return: 元素被加入的index
        """
        i = start
        while i < len(nums1):
            if i >= merged_count:
                nums1[i] = target_num
                break
            elif target_num < nums1[i]:
                for j in range(len(nums1) - 2, i - 1, -1):
                    nums1[j + 1] = nums1[j]

                nums1[i] = target_num
                break

            i += 1

        return i


s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

s.merge(nums1, 3, nums2, 3)
print(nums1)