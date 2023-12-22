# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        if len(preorder) == 2:
            root_node = TreeNode(preorder[0])
            if preorder[0] == inorder[1]:
                left_node = TreeNode(inorder[0])
                root_node.left = left_node
                return root_node
            else:
                right_node = TreeNode(inorder[1])
                root_node.right = right_node
                return root_node

        root = preorder[0]
        root_index_of_inorder = inorder.index(root)
        left_tree_inorder = inorder[:root_index_of_inorder]

        right_tree_inorder = []
        if root_index_of_inorder < len(inorder) - 1:
            right_tree_inorder = inorder[root_index_of_inorder + 1:]

        i = 1
        while i < len(preorder):
            if right_tree_inorder.__contains__(preorder[i]):
                break
            i += 1

        left_tree_preorder = preorder[1: i]
        right_tree_preorder = []
        if i < len(preorder):
            # 确实存在right_tree
            right_tree_preorder = preorder[i:]

        root = TreeNode(root)
        left_tree = self.buildTree(left_tree_preorder, left_tree_inorder)
        right_tree = self.buildTree(right_tree_preorder, right_tree_inorder)
        root.left = left_tree
        root.right = right_tree

        return root