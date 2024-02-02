# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.queue = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.__traverse__(root)

        minimal = 2 ** 32 - 1

        for i in range(len(self.queue) - 1):
            if abs(self.queue[i] - self.queue[i + 1]) < minimal:
                minimal = abs(self.queue[i] - self.queue[i + 1])

        return minimal

    def __traverse__(self, root):
        if root.left is not None:
            self.__traverse__(root.left)

        self.queue.append(root.val)

        if root.right is not None:
            self.__traverse__(root.right)
