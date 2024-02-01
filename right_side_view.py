# https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            queue = [root]
            self.__traverse__(queue)
        return self.result

    def __traverse__(self, queue: List[TreeNode]):
        self.result.append(queue[len(queue) - 1].val)

        next_queue = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                next_queue.append(node.left)
            if node.right is not None:
                next_queue.append(node.right)

        if len(next_queue) > 0:
            self.__traverse__(next_queue)











