# https://leetcode.cn/problems/course-schedule/description/

from typing import List, Set


# DFS版本实现

class GraphNode(object):
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
        self.in_degree = 0

    def add_neighbor(self, neighbor_node: 'GraphNode'):
        self.neighbors.append(neighbor_node)


class Solution:
    def __init__(self):
        self.graph = {1: GraphNode(1)}
        self.visited = []

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [None for _ in range(numCourses + 1)]
        for item in prerequisites:
            self.__build_relation__(item[0], item[1])

        for graph_node in self.graph.values():
            if self.__dfs__(graph_node, []):
                return False
        return True

    def __dfs__(self, node: GraphNode, trace_stack: List[int]) -> bool:
        """
        :return: 有环返回True，无环返回False
        """
        if self.visited[node.val] is not None:
            return self.visited[node.val]

        if node.val in trace_stack:
            self.visited[node.val] = True
            return True

        self.visited.append(node.val)
        trace_stack.append(node.val)
        for neighbor_node in node.neighbors:
            if self.__dfs__(neighbor_node, trace_stack):
                self.visited[node.val] = True
                return True
        trace_stack.pop()
        self.visited[node.val] = False
        return False

    def __build_relation__(self, val1: int, val2: int):
        node1 = self.__get_or_create_node__(val1)
        node2 = self.__get_or_create_node__(val2)
        node1.add_neighbor(node2)
        node2.in_degree += 1

    def __get_or_create_node__(self, val: int):
        if val not in self.graph:
            self.graph[val] = GraphNode(val)
        return self.graph[val]


numCourses = 20
prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
s = Solution()
print(s.canFinish(numCourses, prerequisites))
