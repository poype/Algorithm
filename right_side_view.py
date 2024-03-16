# https://leetcode.cn/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        queue = [root]
        while len(queue) > 0:
            next_queue = []
            result.append(queue[-1].val)

            while len(queue) > 0:
                node = queue.pop(0)
                if node.left is not None:
                    next_queue.append(node.left)

                if node.right is not None:
                    next_queue.append(node.right)

            queue = next_queue

        return result










