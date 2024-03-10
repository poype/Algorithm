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
        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)

        root.left = right_tree
        root.right = left_tree
        return root



