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

        return self.__is_symmetric__(root.left, root.right)

    def __is_symmetric__(self, left_root: TreeNode, right_root: TreeNode) -> bool:
        if left_root is None and right_root is None:
            return True
        elif left_root is None or right_root is None:
            return False
        elif left_root.val != right_root.val:
            return False
        else:
            return (self.__is_symmetric__(left_root.left, right_root.right) and
                    self.__is_symmetric__(left_root.right, right_root.left))
