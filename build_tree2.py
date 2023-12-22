# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        if len(inorder) == 2:
            root = TreeNode(postorder[1])
            if postorder[1] == inorder[1]:
                left_tree = TreeNode(inorder[0])
                root.left = left_tree
            else:
                right_tree = TreeNode(inorder[1])
                root.right = right_tree
            return root

        n = len(inorder)
        root_val = postorder[n - 1]

        root_index_of_inorder = inorder.index(root_val)
        left_inorder = inorder[:root_index_of_inorder]
        right_inorder = []
        if root_index_of_inorder < n - 1:
            right_inorder = inorder[root_index_of_inorder + 1:]

        i = 0
        while i < n - 1:
            if right_inorder.__contains__(postorder[i]):
                break
            i += 1

        left_postorder = postorder[:i]
        right_postorder = []
        if i < n - 1:
            right_postorder = postorder[i: n - 1]

        root_node = TreeNode(root_val)
        left_tree = self.buildTree(left_inorder, left_postorder)
        right_tree = self.buildTree(right_inorder, right_postorder)

        root_node.left = left_tree
        root_node.right = right_tree
        return root_node
