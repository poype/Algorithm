# https://leetcode.cn/problems/binary-tree-inorder-traversal/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        trace = []
        self.inorder_traversal(root, trace)

        return trace

    def inorder_traversal(self, root: TreeNode, trace: List[int]):
        if root.left is not None:
            self.inorder_traversal(root.left, trace)

        trace.append(root.val)

        if root.right is not None:
            self.inorder_traversal(root.right, trace)
