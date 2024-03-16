# https://leetcode.cn/problems/course-schedule/description/

from typing import List


# 拓扑排序版本实现
# 思路是找到入度为0的节点，然后断后与后面节点的链接，并把后面节点的入读都减1
# 最后判断是否所有节点的入度都是0，如果都是0就代表全部课程都能学完，否则就是图有环

class GraphNode(object):
    def __init__(self, val: int):
        self.val = val
        self.neighbors = []
        self.in_degree = 0

    def add_neighbor(self, neighbor_node: 'GraphNode'):
        self.neighbors.append(neighbor_node)


class Solution:
    def __init__(self):
        self.graph = {}

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for item in prerequisites:
            self.__build_relation__(item[0], item[1])

        studied_course = set()
        while True:
            flag = False
            for node in self.graph.values():
                if node.in_degree > 0 or node.val in studied_course:
                    continue

                flag = True
                studied_course.add(node.val)

                for neighbor_node in node.neighbors:
                    neighbor_node.in_degree -= 1

            if not flag:
                break

        for node in self.graph.values():
            if node.in_degree > 0:
                return False
        return True

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
print(s.canFinish(1, []))
