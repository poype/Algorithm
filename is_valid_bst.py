from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.is_valid_bts(root)

    def is_valid_bts(self, root: TreeNode) -> bool:
        if root.left is not None:
            left_max = self.get_max_value_of_root(root.left)
            if root.val <= left_max:
                return False
            if not self.is_valid_bts(root.left):
                return False

        if root.right is not None:
            right_min = self.get_min_value_of_root(root.right)
            if root.val >= right_min:
                return False
            if not self.is_valid_bts(root.right):
                return False

        return True

    def get_max_value_of_root(self, root: TreeNode) -> int:
        """
        获取以root为根节点的子树中的最大值
        """
        left_max, right_max = -9999999999, -9999999999
        if root.left is not None:
            left_max = self.get_max_value_of_root(root.left)
        if root.right is not None:
            right_max = self.get_max_value_of_root(root.right)

        return max(root.val, left_max, right_max)

    def get_min_value_of_root(self, root: TreeNode) -> int:
        """
        获取以root为根节点的子树中的最小值
        """
        left_min, right_min = 9999999999, 9999999999
        if root.left is not None:
            left_min = self.get_min_value_of_root(root.left)
        if root.right is not None:
            right_min = self.get_min_value_of_root(root.right)

        return min(root.val, left_min, right_min)


tnode1 = TreeNode(1)
tnode2 = TreeNode(2)
tnode3 = TreeNode(3)

tnode2.left = tnode1
tnode2.right = tnode3

s = Solution()
print(s.isValidBST(tnode2))
