# https://leetcode.cn/problems/course-schedule-ii/

from typing import List, Dict


class GraphNode(object):
    def __init__(self, val: int):
        self.val = val
        self.neighbors: List['GraphNode'] = []
        self.in_degree = 0

    def add_neighbor(self, neighbor_node: 'GraphNode'):
        self.neighbors.append(neighbor_node)


class Solution:
    def __init__(self):
        self.graph: Dict[int, GraphNode] = {}

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        for i in range(numCourses):
            self.__get_or_create_node__(i)

        for item in prerequisites:
            self.__build_relation__(item[1], item[0])

        queue = []
        while len(queue) < numCourses:
            flag = False
            for node in self.graph.values():
                if node.in_degree == 0 and node.val not in queue:
                    queue.append(node.val)
                    for neighbor_node in node.neighbors:
                        neighbor_node.in_degree -= 1

                    flag = True

            if not flag:
                return []

        return queue

    def __build_relation__(self, val1: int, val2: int):
        node1 = self.__get_or_create_node__(val1)
        node2 = self.__get_or_create_node__(val2)
        node1.add_neighbor(node2)
        node2.in_degree += 1

    def __get_or_create_node__(self, val: int):
        if val not in self.graph:
            self.graph[val] = GraphNode(val)

        return self.graph[val]


s = Solution()
print(s.findOrder(3, [[1, 0], [1, 2]]))
