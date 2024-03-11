# https://leetcode.cn/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_val = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.__traverse__(root, 0)
        return self.sum_val

    def __traverse__(self, root: TreeNode, prefix_num: int):
        num = prefix_num * 10 + root.val
        if root.left is None and root.right is None:
            self.sum_val += num
            return

        if root.left is not None:
            self.__traverse__(root.left, num)
        if root.right is not None:
            self.__traverse__(root.right, num)

