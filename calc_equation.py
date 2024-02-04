# https://leetcode.cn/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class GraphNode:
    def __init__(self, val: str):
        self.val = val
        # key is neighbor node, value is division result
        self.edges = {}

    def add_edge(self, edge_node: str, value: float):
        self.edges[edge_node] = value


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_set = set()
        graph = {}
        # 构造图
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]] = GraphNode(equations[i][0])
            if equations[i][1] not in graph:
                graph[equations[i][1]] = GraphNode(equations[i][1])

            graph[equations[i][0]].add_edge(equations[i][1], values[i])
            graph[equations[i][1]].add_edge(equations[i][0], 1 / values[i])

            node_set.add(equations[i][0])
            node_set.add(equations[i][1])

        result = []
        for query in queries:
            if query[0] not in node_set:
                result.append(-1.00000)
            else:
                result.append(self.__dfs__(query[0], query[1], graph, []))

        return result

    def __dfs__(self, src: str, dest: str, graph: dict[str, GraphNode], traversed: List[str]) -> float:
        traversed.append(src)

        graph_node = graph[src]
        edges = graph_node.edges

        if dest in edges:
            return edges[dest]
        else:
            for key in edges.keys():
                if key not in graph or key in traversed:
                    continue
                result = self.__dfs__(key, dest, graph, traversed)
                if result > 0:
                    return result * edges[key]

        traversed.pop()
        return -1.00000


s = Solution()
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

result = s.calcEquation(equations, values, queries)
print(result)
