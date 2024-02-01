# https://leetcode.cn/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is not None:
            queue = [root]
            self.__traverse__(queue)

        return self.result

    def __traverse__(self, queue: List[TreeNode]):
        avg_value = self.__avg_list__(queue)
        self.result.append(avg_value)

        next_queue = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                next_queue.append(node.left)

            if node.right is not None:
                next_queue.append(node.right)

        if len(next_queue) > 0:
            self.__traverse__(next_queue)

    def __avg_list__(self, l: List[TreeNode]) -> float:
        sum = 0
        for node in l:
            sum += node.val
        return sum / len(l)
