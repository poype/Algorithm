# https://leetcode.cn/problems/maximum-depth-of-binary-tree/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_max, right_max = 0, 0
        if root.left is not None:
            left_max = self.maxDepth(root.left)

        if root.right is not None:
            right_max = self.maxDepth(root.right)

        return max(left_max, right_max) + 1

