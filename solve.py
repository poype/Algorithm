# https://leetcode.cn/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        flag = [[False for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if board[0][i] == 'O' and not flag[0][i]:
                self.__dfs__(board, 0, i, flag)

            if board[m - 1][i] == 'O' and not flag[m - 1][i]:
                self.__dfs__(board, m - 1, i, flag)

        for i in range(m):
            if board[i][0] == 'O' and not flag[i][0]:
                self.__dfs__(board, i, 0, flag)
            if board[i][n - 1] == 'O' and not flag[i][n - 1]:
                self.__dfs__(board, i, n - 1, flag)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not flag[i][j]:
                    board[i][j] = 'X'

    def __dfs__(self, board: List[List[str]], row: int, column: int, flag: List[List[bool]]):
        flag[row][column] = True

        if column < len(board[0]) - 1 and board[row][column + 1] == 'O' and not flag[row][column + 1]:
            self.__dfs__(board, row, column + 1, flag)

        if row < len(board) - 1 and board[row + 1][column] == 'O' and not flag[row + 1][column]:
            self.__dfs__(board, row + 1, column, flag)

        if column > 0 and board[row][column - 1] == 'O' and not flag[row][column - 1]:
            self.__dfs__(board, row, column - 1, flag)

        if row > 0 and board[row - 1][column] == 'O' and not flag[row - 1][column]:
            self.__dfs__(board, row - 1, column, flag)


s = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s.solve(board)
print(board)
