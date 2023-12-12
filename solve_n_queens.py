# https://leetcode.cn/problems/n-queens/

from typing import List

# 思路就是穷举法，从第0行开始，依次向下找每个行中合适的位置
class Solution:
    def __init__(self):
        self.matrix = None
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.matrix = [['.' for _ in range(n)] for _ in range(n)]  # 初始化矩阵
        self.match_n_queens(n, 0)
        return self.result

    def match_n_queens(self, n: int, row: int):
        for column in range(n):
            if self.has_conflict(row, column, n):  # 有冲突就跳过
                continue
            self.matrix[row][column] = 'Q'
            if row == (n - 1):
                self.result.append(self.convert_str_list())
            else:
                self.match_n_queens(n, row + 1)
            self.matrix[row][column] = '.'  # 恢复当前位置，继续尝试本行中的下一列

    def has_conflict(self, row: int, column: int, n: int) -> bool:
        for i in range(0, row):  # 检查列垂直方向
            if self.matrix[i][column] == 'Q':
                return True

        left_column = column - 1
        right_column = column + 1
        for i in range(row - 1, -1, -1):  # 检查斜线方向
            if left_column >= 0 and self.matrix[i][left_column] == 'Q':
                return True

            if right_column < n and self.matrix[i][right_column] == 'Q':
                return True

            left_column = left_column - 1
            right_column = right_column + 1

        return False

    def convert_str_list(self) -> List[str]:  # 将矩阵转换成行字符串的list
        str_list = []
        for row in self.matrix:
            line = "".join(row)
            str_list.append(line)
        return str_list


s = Solution()
print(s.solveNQueens(4))
