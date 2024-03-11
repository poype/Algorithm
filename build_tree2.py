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

        root = TreeNode(postorder[-1])

        i = inorder.index(postorder[-1])
        left_inorder = inorder[0: i]
        right_inorder = inorder[i + 1:]

        j = len(postorder) - 2
        while j >= 0 and postorder[j] not in left_inorder:
            j -= 1
        left_postorder = postorder[:j + 1]
        right_postorder = postorder[j + 1: len(postorder) - 1]

        left_tree = self.buildTree(left_inorder, left_postorder)
        right_tree = self.buildTree(right_inorder, right_postorder)

        root.left = left_tree
        root.right = right_tree
        return root


inorder = [1, 2]
postorder = [2, 1]

s = Solution()
s.buildTree(inorder, postorder)
