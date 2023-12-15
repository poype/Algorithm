# https://leetcode.cn/problems/redundant-connection/description/

from typing import List, Set


# 此题虽然是有向图，但要把它当成无向图来看待
# 也是先在无向图中找到一个环，然后删除环中的一个边，但要注意的是，如果环中存在某个节点的入度大于1，则一定要删除与那个节点的边
# 此外要特殊处理 a -> b and a <- b 这种互相指向的case，因为判断环的算法无法找出这种环
# 所以此题基本上是在 684. 冗余连接 的基础上的微调

class Node(object):
    def __init__(self, num: int):
        self.num = num
        self.edges = set()

    def add_edge(self, edge):
        self.edges.add(edge)


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # 题目中说明是比树多一条边，所以节点数量与边的数量相同

        node_list = []
        for i in range(n + 1):
            node_list.append(Node(i))

        in_degree_list = [0 for _ in range(n + 1)]
        # 构造图
        for edge in edges:
            node_list[edge[0]].add_edge(node_list[edge[1]])
            node_list[edge[1]].add_edge(node_list[edge[0]])
            in_degree_list[edge[1]] += 1

        in_degree_lg_1_node = -1
        # 存在一个入度为0的node，证明没有环
        for i in range(1, n + 1):
            if in_degree_list[i] > 1:
                in_degree_lg_1_node = i

        # 下面dfs遍历去找环
        none_node = Node(-1)  # 标记node，代表None
        for i in range(n):
            trace = []
            if self.dfs(node_list[i], none_node, trace):
                last_trace = trace.pop()
                while trace[0] != last_trace:
                    trace.remove(trace[0])
                return self.find_last_edge(trace, edges, in_degree_lg_1_node)

        for i in range(len(edges)):
            for j in range(i, len(edges)):
                if edges[i][0] == edges[j][1] and edges[i][1] == edges[j][0]:
                    trace = edges[i][:]
                    return self.find_last_edge(trace, edges, in_degree_lg_1_node)

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

    def find_last_edge(self, trace: List, edges: List[List[int]], in_degree_lg_1_node: int):
        max_pos = -1
        result = [0, 0]
        for i in range(len(trace)):
            if i == len(trace) - 1:  # 最后一个节点能跟第一个节点组成边
                trace_edge = [trace[i], trace[0]]
            else:
                trace_edge = trace[i:i + 2]
            trace_edge.sort()
            for j in range(len(edges)):
                edge = edges[j][:]
                edge.sort()
                if trace_edge[0] == edge[0] and trace_edge[1] == edge[1] and j > max_pos:
                    if in_degree_lg_1_node != -1 and edges[j][1] != in_degree_lg_1_node:  # 一旦有入度大于1的节点，则必须删除与那个节点相关的边
                        continue

                    max_pos = j
                    result[0] = edges[j][0]
                    result[1] = edges[j][1]

        return result


s = Solution()
print(s.findRedundantDirectedConnection([[4, 2], [1, 5], [5, 2], [5, 3], [2, 4]]))
