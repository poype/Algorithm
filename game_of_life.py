# https://leetcode.cn/problems/game-of-life/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        switch_flags = []

        for i in range(m):
            for j in range(n):
                live_neighbors = self.sum_neighbors(i, j, m, n, board)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    switch_flags.append([i, j])
                elif board[i][j] == 0 and live_neighbors == 3:
                    switch_flags.append([i, j])

        while len(switch_flags) > 0:
            pos = switch_flags.pop()
            if board[pos[0]][pos[1]] == 1:
                board[pos[0]][pos[1]] = 0
            else:
                board[pos[0]][pos[1]] = 1

    def sum_neighbors(self, i: int, j: int, m: int, n: int, board: List[List[int]]) -> int:
        """
        :param i: 第 i 行
        :param j: 第 j 列
        :param m: board的行数
        :param n: board的列数
        :return: 周围8个节点的sum
        """
        result = 0
        if i > 0 and j > 0:
            result += board[i - 1][j - 1]  # 左上角
        if i > 0:
            result += board[i - 1][j]  # 上
        if j > 0:
            result += board[i][j - 1]  # 左
        if i < m - 1 and j < n - 1:
            result += board[i + 1][j + 1]  # 右下角
        if i < m - 1:
            result += board[i + 1][j]  # 下
        if j < n - 1:
            result += board[i][j + 1]  # 右
        if i < m - 1 and j > 0:
            result += board[i + 1][j - 1]  # 左下角
        if i > 0 and j < n - 1:
            result += board[i - 1][j + 1]  # 右上角

        return result


s = Solution()
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
s.gameOfLife(board)

print(board)