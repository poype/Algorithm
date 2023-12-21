# https://leetcode.cn/problems/binary-tree-level-order-traversal/

from typing import Optional, List, Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[TreeNode]]:
        if root is None:
            return []

        result = []
        level_node = [root]
        while len(level_node) > 0:
            level_num = []
            for e in level_node:
                level_num.append(e.val)
            result.append(level_num)

            next_level_node = []
            while len(level_node) > 0:
                node = level_node.pop(0)
                if node.left is not None:
                    next_level_node.append(node.left)
                if node.right is not None:
                    next_level_node.append(node.right)

            level_node = next_level_node
        return result
