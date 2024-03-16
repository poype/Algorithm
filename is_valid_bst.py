from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        is_valid, maximum, minimum = self.__is_valid_bst__(root) # 一次接收函数返回的多个值
        return is_valid

    def __is_valid_bst__(self, root: TreeNode) -> (bool, int, int):  # 一次返回多个结果
        """
        :return: (是否是BST，最大值，最小值)
        """
        if root.left is None and root.right is None:
            return True, root.val, root.val

        minimum, maximum = root.val, root.val
        if root.left is not None:
            left_valid, left_maximum, left_minimum = self.__is_valid_bst__(root.left)
            if not left_valid:
                return False, None, None
            if root.val <= left_maximum:
                return False, None, None
            minimum = left_minimum

        if root.right is not None:
            right_valid, right_maximum, right_minimum = self.__is_valid_bst__(root.right)
            if not right_valid:
                return False, None, None
            if root.val >= right_minimum:
                return False, None, None
            maximum = right_maximum

        return True, maximum, minimum


tnode1 = TreeNode(5)
tnode2 = TreeNode(1)
tnode3 = TreeNode(4)
tnode4 = TreeNode(3)
tnode5 = TreeNode(6)

tnode1.left = tnode2
tnode1.right = tnode3
tnode3.left = tnode4
tnode3.right = tnode5

s = Solution()
print(s.isValidBST(tnode1))
