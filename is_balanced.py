# https://leetcode.cn/problems/balanced-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.is_balance_tree(root)

    def is_balance_tree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        left_height, right_height = 0, 0
        if root.left is not None:
            left_height = self.calculate_height(root.left)

        if root.right is not None:
            right_height = self.calculate_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balance_tree(root.left) and self.is_balance_tree(root.right)

    def calculate_height(self, root: TreeNode) -> int:

        left_height, right_height = 0, 0
        if root.left is not None:
            left_height = self.calculate_height(root.left)

        if root.right is not None:
            right_height = self.calculate_height(root.right)

        return max(left_height, right_height) + 1
