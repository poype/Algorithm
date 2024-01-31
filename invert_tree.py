# https://leetcode.cn/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left_root, right_root = None, None
        if root.left is not None:
            left_root = self.invertTree(root.left)

        if root.right is not None:
            right_root = self.invertTree(root.right)

        root.left = right_root
        root.right = left_root

        return root



