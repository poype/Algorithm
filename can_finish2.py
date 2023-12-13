# https://leetcode.cn/problems/course-schedule/description/

from typing import List

# 拓扑排序版本实现
# 思路是找到入度为0的节点，然后断后与后面节点的链接，并把后面节点的入读都减1
# 最后判断是否所有节点的入度都是0，如果都是0就代表全部课程都能学完，否则就是图有环

class GraphNode(object):
    def __init__(self, course: int):
        self.course = course
        self.post_courses = []

    def add_post_course(self, course_node):
        self.post_courses.append(course_node)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 记录每个课程的入度
        course_in_degree_list = [0 for _ in range(numCourses)]
        course_list = []
        for i in range(numCourses):
            course_list.append(GraphNode(i))

        for relation in prerequisites:  # 构造图
            pre_course = course_list[relation[0]]
            post_course = course_list[relation[1]]
            pre_course.add_post_course(post_course)
            course_in_degree_list[relation[1]] += 1

        for i in range(len(course_in_degree_list)):
            queue = []
            if course_in_degree_list[i] == 0:
                queue.append(i)
                while len(queue) > 0:
                    study_course = queue.pop()
                    post_courses = course_list[study_course].post_courses
                    while len(post_courses) > 0:
                        post_course = post_courses.pop()  # 使用pop是为了断开这个链接，必须要断开链接，否则会重复计算
                        course_in_degree_list[post_course.course] -= 1
                        if course_in_degree_list[post_course.course] == 0:
                            queue.append(post_course.course)

        for in_degree in course_in_degree_list:
            if in_degree != 0:
                return False
        return True


s = Solution()
print(s.canFinish(3, [[0,1],[0,2],[1,2]]))
