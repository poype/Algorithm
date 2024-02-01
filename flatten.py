# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root

        queue = []
        self.traverse(queue, root)

        for i in range(len(queue) - 1):
            queue[i].left = None
            queue[i].right = queue[i + 1]

        queue[len(queue) - 1].left = None
        queue[len(queue) - 1].right = None

    def traverse(self, queue: List[TreeNode], root: TreeNode):  # 注意traverse单词的拼写
        queue.append(root)
        if root.left is not None:
            self.traverse(queue, root.left)

        if root.right is not None:
            self.traverse(queue, root.right)
