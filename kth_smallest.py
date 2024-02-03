# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cnt = 0
        self.result = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0

        self.__traverse__(root, k)
        return self.result

    def __traverse__(self, root: TreeNode, k: int):
        if self.cnt == k:
            return

        if root.left is not None:
            self.__traverse__(root.left, k)

        self.cnt += 1
        if self.cnt == k:
            self.result = root.val

        if root.right is not None:
            self.__traverse__(root.right, k)
