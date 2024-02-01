# https://leetcode.cn/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = []
        self.idx = 0
        if root is not None:
            self.__traverse__(root)

    def __traverse__(self, root: TreeNode):
        if root.left is not None:
            self.__traverse__(root.left)

        self.queue.append(root.val)

        if root.right is not None:
            self.__traverse__(root.right)

    def next(self) -> int:
        val = self.queue[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.queue)
