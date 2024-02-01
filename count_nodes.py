# https://leetcode.cn/problems/count-complete-tree-nodes/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.count = 0

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.__traverse__(root)
        return self.count

    def __traverse__(self, root: TreeNode):
        self.count += 1

        if root.left is not None:
            self.__traverse__(root.left)

        if root.right is not None:
            self.__traverse__(root.right)
