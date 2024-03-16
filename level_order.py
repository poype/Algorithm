# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import Optional, List, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = [root]
        while len(queue) > 0:
            result.append(self.__convert__(queue))

            next_queue = []
            while len(queue) > 0:
                node = queue.pop(0)

                if node.left is not None:
                    next_queue.append(node.left)
                if node.right is not None:
                    next_queue.append(node.right)

            queue = next_queue

        return result

    def __convert__(self, queue: List[TreeNode]):
        num_queue = []
        for node in queue:
            num_queue.append(node.val)
        return num_queue


root = TreeNode(1)
s = Solution()
s.levelOrder(root)
