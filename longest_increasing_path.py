# https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/


from typing import List


class StepCounter:
    def __init__(self):
        self.max_step_count = 0
        self.step_count = 0

    def add(self):
        self.step_count += 1
        if self.step_count > self.max_step_count:
            self.max_step_count = self.step_count

    def minus(self):
        self.step_count -= 1


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        step_counter = StepCounter()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, step_counter)

        return step_counter.max_step_count + 1

    def dfs(self, matrix: List[List[int]], i: int, j: int, step_counter: StepCounter):
        """
        :param matrix: 矩阵
        :param i: 行号
        :param j: 列号
        :param step_counter: 步数计数器
        """
        # 向左走
        if j > 0 and matrix[i][j] < matrix[i][j - 1]:
            step_counter.add()
            self.dfs(matrix, i, j - 1, step_counter)
            step_counter.minus()

        # 向右走
        if j < len(matrix[0]) - 1 and matrix[i][j] < matrix[i][j + 1]:
            step_counter.add()
            self.dfs(matrix, i, j + 1, step_counter)
            step_counter.minus()

        # 向上走
        if i > 0 and matrix[i][j] < matrix[i - 1][j]:
            step_counter.add()
            self.dfs(matrix, i - 1, j, step_counter)
            step_counter.minus()

        # 向下走
        if i < len(matrix) - 1 and matrix[i][j] < matrix[i + 1][j]:
            step_counter.add()
            self.dfs(matrix, i + 1, j, step_counter)
            step_counter.minus()


s = Solution()
matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]

print(s.longestIncreasingPath(matrix))
