# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        if n == 2:
            root = TreeNode(nums[0])
            right_tree = TreeNode(nums[1])
            root.right = right_tree
            return root

        mid = n // 2
        left_nums = nums[0: mid]
        right_nums = nums[(mid + 1):]

        root = TreeNode(nums[mid])
        left_tree = self.sortedArrayToBST(left_nums)
        right_tree = self.sortedArrayToBST(right_nums)
        root.left = left_tree
        root.right = right_tree

        return root
