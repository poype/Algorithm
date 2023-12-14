# https://leetcode.cn/problems/course-schedule-ii/

from typing import List


# 类似于BFS，拓扑排序

class GraphNode(object):
    def __init__(self, course: int):
        self.course = course
        self.post_courses = []

    def add_post_course(self, course_node):
        self.post_courses.append(course_node)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        course_order_list = []

        course_list = []
        for i in range(numCourses):
            course_list.append(GraphNode(i))

        in_degree_list = [0 for _ in range(numCourses)]
        for relation in prerequisites:
            pre_course = course_list[relation[1]]
            post_course = course_list[relation[0]]
            pre_course.add_post_course(post_course)
            in_degree_list[relation[0]] += 1

        for i in range(len(in_degree_list)):
            stack = []
            if in_degree_list[i] == 0 and not course_order_list.__contains__(i):
                stack.append(i)
                while len(stack) > 0:
                    study_course_num = stack.pop()
                    course_order_list.append(study_course_num)

                    post_courses = course_list[study_course_num].post_courses
                    while len(post_courses) > 0:
                        post_course = post_courses.pop()
                        in_degree_list[post_course.course] -= 1
                        if in_degree_list[post_course.course] == 0:
                            stack.append(post_course.course)

        for in_degree in in_degree_list:  # 有环返回空list
            if in_degree > 0:
                return []
        return course_order_list


s = Solution()
print(s.findOrder(3, [[1, 0], [1, 2], [0, 1]]))
