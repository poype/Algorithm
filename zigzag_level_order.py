# https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result

        queue = [root]
        flag = False
        while len(queue) > 0:
            next_queue = []
            result.append(self.__convert__(queue))

            while len(queue) > 0:
                node = queue.pop()
                if flag:
                    if node.left is not None:
                        next_queue.append(node.left)

                    if node.right is not None:
                        next_queue.append(node.right)
                else:
                    if node.right is not None:
                        next_queue.append(node.right)

                    if node.left is not None:
                        next_queue.append(node.left)

            flag = not flag

            queue = next_queue

        return result

    def __convert__(self, queue: List[TreeNode]):
        num_queue = []
        for node in queue:
            num_queue.append(node.val)
        return num_queue
