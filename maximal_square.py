# https://leetcode.cn/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self):
        self.maximal_square = 0
        self.cache = set()

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.__maximal_square__(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        return self.maximal_square

    def __maximal_square__(self, matrix: List[List[str]], start_row, start_column, end_row, end_column):
        if f"{start_row}_{start_column}_{end_row}_{end_column}" in self.cache:
            return
        self.cache.add(f"{start_row}_{start_column}_{end_row}_{end_column}")

        row_length = end_row - start_row + 1
        column_length = end_column - start_column + 1

        if row_length > column_length:
            self.__maximal_square__(matrix, start_row + 1, start_column, end_row, end_column)
            self.__maximal_square__(matrix, start_row, start_column, end_row - 1, end_column)
        elif column_length > row_length:
            self.__maximal_square__(matrix, start_row, start_column + 1, end_row, end_column)
            self.__maximal_square__(matrix, start_row, start_column, end_row, end_column - 1)
        else:
            flag = True
            for i in range(start_row, end_row + 1):
                for j in range(start_column, end_column + 1):
                    if matrix[i][j] == '0':
                        flag = False
                        self.__maximal_square__(matrix, start_row + 1, start_column + 1, end_row, end_column)
                        self.__maximal_square__(matrix, start_row, start_column, end_row - 1, end_column - 1)
                        self.__maximal_square__(matrix, start_row, start_column + 1, end_row - 1, end_column)
                        self.__maximal_square__(matrix, start_row + 1, start_column, end_row, end_column - 1)
                        break

            if flag:
                square = (end_row - start_row + 1) ** 2
                if square > self.maximal_square:
                    self.maximal_square = square


s = Solution()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(s.maximalSquare(matrix))
