# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 思路： 依次计算以树中每个节点为root的最大值，则这个最大值有下面几种可能：
# 1. 经过root， max(left + root, right + root, left + right + root)
# 2. 不经过root, max(left, right)
class Solution:
    def __init__(self):
        self.max_val = -(2 ** 32)  # 最小值

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.__traverse__(root)
        return self.max_val

    def __traverse__(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            if root.val > self.max_val:
                self.max_val = root.val
            return root.val

        left_max_val, right_max_val = -(2 ** 32), -(2 ** 32)
        if root.left is not None:
            left_max_val = self.__traverse__(root.left)

        if root.right is not None:
            right_max_val = self.__traverse__(root.right)

        root_max_val = max(left_max_val, right_max_val, left_max_val + root.val,
                           right_max_val + root.val, left_max_val + root.val + right_max_val, root.val)
        if root_max_val > self.max_val:
            self.max_val = root_max_val

        return max(left_max_val + root.val, right_max_val + root.val, root.val) # 注意这里return的值跟上面的max不一样


tree_node1 = TreeNode(5)
tree_node2 = TreeNode(4)
tree_node3 = TreeNode(8)

tree_node1.left = tree_node2
tree_node1.right = tree_node3

tree_node4 = TreeNode(11)
tree_node5 = TreeNode(13)
tree_node6 = TreeNode(4)
tree_node2.left = tree_node4
tree_node3.left = tree_node5
tree_node3.right = tree_node6

tree_node7 = TreeNode(7)
tree_node8 = TreeNode(2)
tree_node9 = TreeNode(1)

tree_node4.left = tree_node7
tree_node4.right = tree_node8
tree_node6.right = tree_node9

s = Solution()
print(s.maxPathSum(tree_node1))
