# https://leetcode.cn/problems/clone-graph/description/
import copy


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional, List


class Solution:
    def __init__(self):
        self.copied_edge_list = []
        self.node_dict = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        return self.dfs(node, None, None)

    def dfs(self, current_node: Node, from_node: Node, new_from_node: Node):
        if from_node is not None:
            edge = [current_node.val, from_node.val]
            edge.sort()
            if self.exist_edge(edge):
                return None

        new_node = self.createOrGetNode(current_node.val)
        if new_from_node is not None:
            new_from_node.neighbors.append(new_node)
            new_node.neighbors.append(new_from_node)
            new_edge = [new_node.val, new_from_node.val]
            new_edge.sort()
            self.copied_edge_list.append(new_edge)

        for neighbor_node in current_node.neighbors:
            if neighbor_node == from_node:
                continue
            self.dfs(neighbor_node, current_node, new_node)

        return new_node

    def exist_edge(self, edge: List) -> bool:
        for copied_edge in self.copied_edge_list:
            if copied_edge[0] == edge[0] and copied_edge[1] == edge[1]:
                return True
        return False

    def createOrGetNode(self, val: int) -> Node:
        if self.node_dict.__contains__(val):
            return self.node_dict[val]

        new_node = Node(val)
        self.node_dict[val] = new_node
        return new_node




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors.append(node2)
node2.neighbors.append(node1)

node1.neighbors.append(node4)
node4.neighbors.append(node1)

node3.neighbors.append(node4)
node4.neighbors.append(node3)

node3.neighbors.append(node2)
node2.neighbors.append(node3)

s = Solution()
new_node2 = s.cloneGraph(node1)

print("end")


class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        return copy.deepcopy(node)