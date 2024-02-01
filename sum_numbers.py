# https://leetcode.cn/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.traverse(root, 0)
        return self.sum

    def traverse(self, root: TreeNode, num: int):
        num = num * 10 + root.val

        if root.left is None and root.right is None:
            self.sum += num

        if root.left is not None:
            self.traverse(root.left, num)
        if root.right is not None:
            self.traverse(root.right, num)
