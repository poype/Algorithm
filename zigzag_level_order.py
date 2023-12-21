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

        node_stack = []
        node_stack.append(root)
        flag = 0
        while len(node_stack) > 0:
            num_list = []
            new_node_stack = []
            while len(node_stack) > 0:
                tree_node = node_stack.pop()
                num_list.append(tree_node.val)

                if flag % 2 == 1:
                    if tree_node.right is not None:
                        new_node_stack.append(tree_node.right)
                    if tree_node.left is not None:
                        new_node_stack.append(tree_node.left)
                else:
                    if tree_node.left is not None:
                        new_node_stack.append(tree_node.left)
                    if tree_node.right is not None:
                        new_node_stack.append(tree_node.right)

            result.append(num_list)
            flag += 1
            node_stack = new_node_stack

        return result

