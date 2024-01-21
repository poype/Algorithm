# https://leetcode.cn/problems/set-matrix-zeroes/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self):
        self.column_num_set = set()
        self.row_num_set = set()

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.row_num_set.add(i)
                    self.column_num_set.add(j)

        for row_num in self.row_num_set:
            self.set_row(matrix, row_num)

        for column_row in self.column_num_set:
            self.set_column(matrix, column_row)

    def set_row(self, matrix: List[List[int]], row_num: int):
        column_cnt = len(matrix[0])
        for i in range(column_cnt):
            matrix[row_num][i] = 0

    def set_column(self, matrix: List[List[int]], column_num: int):
        row_cnt = len(matrix)
        for i in range(row_cnt):
            matrix[i][column_num] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s = Solution()
s.setZeroes(matrix)
print(matrix)
