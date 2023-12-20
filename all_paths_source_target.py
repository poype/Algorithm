# https://leetcode.cn/problems/all-paths-from-source-to-target/


from typing import List

class GraphNode:
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, neighbor_node):
        self.neighbors.append(neighbor_node)

class Solution:
    def __init__(self):
        self.graph_node_dict = {}
        self.result = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        for i in range(len(graph)):
            node = self.create_or_get_node(i)
            for neighbor_val in graph[i]:
                neighbor_node = self.create_or_get_node(neighbor_val)
                node.add_neighbor(neighbor_node)

        self.dfs(self.create_or_get_node(0), self.create_or_get_node(len(graph) - 1), [])
        return self.result

    def dfs(self, current_node: GraphNode, target_node: GraphNode, trace: List[int]):
        trace.append(current_node.val)
        if current_node == target_node:
            self.result.append(trace[:])
            trace.pop()
            return

        for node in current_node.neighbors:
            self.dfs(node, target_node, trace)

        trace.pop()

    def create_or_get_node(self, val: int):
        if not self.graph_node_dict.__contains__(val):
            self.graph_node_dict[val] = GraphNode(val)

        return self.graph_node_dict[val]


s = Solution()
result = s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])
print(result)