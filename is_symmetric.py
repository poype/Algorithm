# https://leetcode.cn/problems/symmetric-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.is_same_tree(root.left, root.right)

    def is_same_tree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False

        if p.val != q.val:
            return False

        if not self.is_same_tree(p.left, q.right):  # 这里是left 和 right去去比较
            return False
        if not self.is_same_tree(p.right, q.left):
            return False

        return True


