# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.__build_tree__(preorder, inorder)

    def __build_tree__(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        i = inorder.index(preorder[0])

        left_inorder = inorder[0:i]
        right_inorder = inorder[i + 1:]

        j = 1
        while j < len(preorder) and preorder[j] not in right_inorder:
            j += 1

        left_preorder = preorder[1:j]
        right_preorder = preorder[j:]

        left_tree = self.__build_tree__(left_preorder, left_inorder)
        right_tree = self.__build_tree__(right_preorder, right_inorder)

        root.left = left_tree
        root.right = right_tree
        return root
