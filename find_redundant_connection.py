# https://leetcode.cn/problems/redundant-connection/description/

from typing import List, Set


class Node(object):
    def __init__(self, num: int):
        self.num = num
        self.edges = set()

    def add_edge(self, edge):
        self.edges.add(edge)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # 题目中说明是比树多一条边，所以节点数量与边的数量相同

        node_list = []
        for i in range(n + 1):
            node_list.append(Node(i))

        # 构造图
        for edge in edges:
            node_list[edge[0]].add_edge(node_list[edge[1]])
            node_list[edge[1]].add_edge(node_list[edge[0]])

        # 下面dfs遍历去找环
        none_node = Node(-1)  # 标记node，代表None
        for i in range(n):
            trace = []
            if self.dfs(node_list[i], none_node, trace):
                last_trace = trace.pop()
                while trace[0] != last_trace:
                    trace.remove(trace[0])
                return self.find_last_edge(trace, edges)

    def dfs(self, node: Node, from_node: Node, trace: List) -> bool:
        if trace.__contains__(node.num):
            trace.append(node.num)
            return True

        trace.append(node.num)

        for edge_node in node.edges:
            if edge_node == from_node:  # 由于是无向图，要确保不能走回头路
                continue

            if self.dfs(edge_node, node, trace):
                return True

        trace.remove(node.num)
        return False

    def find_last_edge(self, trace: List, edges: List[List[int]]):
        max_pos = -1
        result = [0, 0]
        for i in range(len(trace)):
            if i == len(trace) - 1:  # 最后一个节点能跟第一个节点组成边
                trace_edge = [trace[i], trace[0]]
            else:
                trace_edge = trace[i:i + 2]
            trace_edge.sort()
            for j in range(len(edges)):
                if trace_edge[0] == edges[j][0] and trace_edge[1] == edges[j][1] and j > max_pos:
                    max_pos = j
                    result[0] = trace_edge[0]
                    result[1] = trace_edge[1]

        return result


s = Solution()
print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
