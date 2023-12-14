# https://leetcode.cn/problems/redundant-connection-ii/

from typing import List


class Node(object):
    def __init__(self, num: int):
        self.num = num
        self.edges = set()

    def add_edge(self, edge):
        self.edges.add(edge)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        node_list = []
        for i in range(n + 1):
            node_list.append(Node(i))

        # 构造图
        in_degree_list = [0 for _ in range(n + 1)]
        for edge in edges:
            node_list[edge[0]].add_edge(node_list[edge[1]])
            in_degree_list[edge[1]] += 1

        in_degree_lg_1_node = -1
        in_degree_eq_0_node = -1
        # 存在一个入度为0的node，证明没有环
        for i in range(1, n + 1):
            if in_degree_list[i] == 0:
                in_degree_eq_0_node = i
            if in_degree_list[i] > 1:
                in_degree_lg_1_node = i

        if in_degree_lg_1_node != -1:
            for j in range(len(edges) - 1, -1, -1):
                if edges[j][1] == in_degree_lg_1_node and edges[j][0] != in_degree_eq_0_node:
                    return edges[j]

        if in_degree_eq_0_node != -1:
            for j in range(len(edges) - 1, -1, -1):
                if edges[j][0] != in_degree_eq_0_node:  # 如果存在入度为0的节点，除了与该节点相关联的边外，其它的边随便删一个
                    return edges[j]

        # 不存在入度为0的node，图中存在环
        for i in range(n):
            trace = []
            if self.dfs(node_list[i], trace):
                last_trace = trace.pop()
                while trace[0] != last_trace:
                    trace.remove(trace[0])

                for k in range(len(trace)):  # 入度大于1的点一定
                    if in_degree_list[trace[k]] > 1:
                        return [trace[k - 1], trace[k]]

                return self.find_last_edge(trace, edges)

    def dfs(self, node: Node, trace: List) -> bool:
        if trace.__contains__(node.num):
            trace.append(node.num)
            return True

        trace.append(node.num)

        for edge_node in node.edges:
            if self.dfs(edge_node, trace):
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
            for j in range(len(edges)):
                if trace_edge[0] == edges[j][0] and trace_edge[1] == edges[j][1] and j > max_pos:
                    max_pos = j
                    result[0] = trace_edge[0]
                    result[1] = trace_edge[1]
        return result


s = Solution()
print(s.findRedundantDirectedConnection([[4,2],[1,5],[5,2],[5,3],[2,4]]))
