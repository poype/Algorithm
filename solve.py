# https://leetcode.cn/problems/surrounded-regions/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return

        m = len(board)
        n = len(board[0])

        flag = [[False for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if board[0][i] == 'O' and not flag[0][i]:
                self.dfs(0, i, board, flag)
            if board[m - 1][i] == 'O' and not flag[m - 1][i]:
                self.dfs(m - 1, i, board, flag)

        for i in range(m):
            if board[i][0] == 'O' and not flag[i][0]:
                self.dfs(i, 0, board, flag)
            if board[i][n - 1] == 'O' and not flag[i][n - 1]:
                self.dfs(i, n - 1, board, flag)

        for i in range(m):
            for j in range(n):
                if not flag[i][j]:
                    board[i][j] = 'X'

    def dfs(self, row: int, column: int, board: List[List[str]], flag: List[List[int]]):
        flag[row][column] = True

        if row > 1 and not flag[row - 1][column] and board[row - 1][column] == 'O':
            self.dfs(row - 1, column, board, flag)
        if row < len(board) - 1 and not flag[row + 1][column] and board[row + 1][column] == 'O':
            self.dfs(row + 1, column, board, flag)
        if column > 1 and not flag[row][column - 1] and board[row][column - 1] == 'O':
            self.dfs(row, column - 1, board, flag)
        if column < len(board[0]) - 1 and not flag[row][column + 1] and board[row][column + 1] == 'O':
            self.dfs(row, column + 1, board, flag)


s = Solution()
board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
s.solve(board)
print(board)
