# https://leetcode.cn/problems/number-of-islands/
from typing import List


class Solution:
    def __init__(self):
        self.flag = [[]]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)  # 行数
        if m == 0:
            return 0

        n = len(grid[0])  # 列数

        self.flag = [[False for _ in range(n)] for _ in range(m)]

        island_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not self.flag[i][j]:
                    island_num += 1
                self.dfs(grid, i, j, m, n, -1, -1)
        return island_num

    def dfs(self, grid: List[List[str]], i: int, j: int, m: int, n: int, from_i: int, from_j: int):
        if grid[i][j] == '0':
            return

        if self.flag[i][j]:
            return

        self.flag[i][j] = True

        if i > 0 and grid[i - 1][j] == '1' and (i - 1) != from_i:
            self.dfs(grid, i - 1, j, m, n, i, j)
        if j < n - 1 and grid[i][j + 1] == '1' and (j + 1) != from_j:
            self.dfs(grid, i, j + 1, m, n, i, j)
        if i < m - 1 and grid[i + 1][j] == '1' and (i + 1) != from_i:
            self.dfs(grid, i + 1, j, m, n, i, j)
        if j > 0 and grid[i][j - 1] == '1' and (j - 1) != from_j:
            self.dfs(grid, i, j - 1, m, n, i, j)


s = Solution()
grid = [["1"],["1"]]

print(s.numIslands(grid))