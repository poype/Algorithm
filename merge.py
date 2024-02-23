# https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        p = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p], nums1[i] = nums1[i], nums1[p]  # 交换
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        while j >= 0:
            nums1[p] = nums2[j]
            p -= 1
            j -= 1


s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

s.merge(nums1, 3, nums2, 3)
print(nums1)