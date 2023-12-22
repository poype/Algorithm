# https://leetcode.cn/problems/binary-tree-maximum-path-sum/
from typing import Optional, List

# 思路是先向一棵树转换成一个无向图，然后计算无向图中从每个节点开始的max path
# 这个代码会time limit，但是逻辑是对的  不再优化了
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


class Solution:
    def __init__(self):
        self.graph_node_list = []
        self.max_sum = -99999999

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.build_graph(root)

        for graph_node in self.graph_node_list:
            self.dfs(graph_node, 0, None)

        return self.max_sum

    def dfs(self, current_node: GraphNode, sum_val: int, from_node: GraphNode):
        sum_val += current_node.val
        if sum_val > self.max_sum:
            self.max_sum = sum_val

        for neighbor in current_node.neighbors:
            if neighbor == from_node:
                continue
            self.dfs(neighbor, sum_val, current_node)

    def build_graph(self, root: TreeNode) -> GraphNode:
        graph_node = self.create_graph_node(root.val)
        if root.left is not None:
            left_neighbor = self.build_graph(root.left)
            graph_node.add_neighbor(left_neighbor)
            left_neighbor.add_neighbor(graph_node)
        if root.right is not None:
            right_neighbor = self.build_graph(root.right)
            graph_node.add_neighbor(right_neighbor)
            right_neighbor.add_neighbor(graph_node)

        return graph_node

    def create_graph_node(self, val: int) -> GraphNode:
        node = GraphNode(val)
        self.graph_node_list.append(node)
        return node


tree_node1 = TreeNode(0)
tree_node2 = TreeNode(1)
tree_node3 = TreeNode(1)

tree_node1.left = tree_node2
tree_node1.right = tree_node3

s = Solution()
print(s.maxPathSum(tree_node1))