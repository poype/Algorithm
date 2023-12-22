# https://leetcode.cn/problems/path-sum-ii/
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []

        return self.find_path(root, targetSum)

    def find_path(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        if root.left is None and root.right is None:
            if root.val == target_sum:
                return [[root.val]]
            else:
                return []

        result = []
        if root.left is not None:
            left_result = self.find_path(root.left, target_sum - root.val)
            result.extend(left_result)
        if root.right is not None:
            right_result = self.find_path(root.right, target_sum - root.val)
            result.extend(right_result)

        if len(result) == 0:
            return []

        for item in result:
            item.insert(0, root.val)

        return result
