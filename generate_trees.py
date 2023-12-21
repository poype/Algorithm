# https://leetcode.cn/problems/unique-binary-search-trees-ii/

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        arr = []
        for i in range(1, n + 1):
            arr.append(i)

        result = []
        for i in range(n):
            part_result = self.create_order_tree(arr[i], arr[:i], arr[i + 1:])
            result.extend(part_result)

        return result

    def create_order_tree(self, root: int, left_list: List[int], right_list: List[int]) -> List[TreeNode]:
        left_tree_list, right_tree_list = [], []
        if len(left_list) > 0:
            for i in range(len(left_list)):
                one_left_tree_list = self.create_order_tree(left_list[i], left_list[:i], left_list[i + 1:])
                left_tree_list.extend(one_left_tree_list)

        if len(right_list) > 0:
            for i in range(len(right_list)):
                one_right_tree_list = self.create_order_tree(right_list[i], right_list[:i], right_list[i + 1:])
                right_tree_list.extend(one_right_tree_list)

        result = []
        if len(left_tree_list) == 0 and len(right_tree_list) == 0:
            result.append(TreeNode(root))
        elif len(left_tree_list) == 0:
            for right_tree in right_tree_list:
                root_node = TreeNode(root)
                root_node.right = right_tree
                result.append(root_node)
        elif len(right_tree_list) == 0:
            for left_tree in left_tree_list:
                root_node = TreeNode(root)
                root_node.left = left_tree
                result.append(root_node)
        else:
            for i in range(len(left_tree_list)):
                for j in range(len(right_tree_list)):
                    root_node = TreeNode(root)
                    root_node.left = left_tree_list[i]
                    root_node.right = right_tree_list[j]
                    result.append(root_node)

        return result


s = Solution()
tree_list = s.generateTrees(4)
print(tree_list)
