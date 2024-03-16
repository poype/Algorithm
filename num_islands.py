# https://leetcode.cn/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        flag = [[False for _ in range(n)] for _ in range(m)]

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not flag[i][j]:
                    cnt += 1
                    self.__dfs__(grid, i, j, flag)

        return cnt

    def __dfs__(self, grid: List[List[str]], row: int, column: int, flag: List[List[bool]]):
        flag[row][column] = True

        if column < len(grid[0]) - 1 and grid[row][column + 1] == '1' and not flag[row][column + 1]:
            self.__dfs__(grid, row, column + 1, flag)

        if row < len(grid) - 1 and grid[row + 1][column] == '1' and not flag[row + 1][column]:
            self.__dfs__(grid, row + 1, column, flag)

        if column > 0 and grid[row][column - 1] == '1' and not flag[row][column - 1]:
            self.__dfs__(grid, row, column - 1, flag)

        if row > 0 and grid[row - 1][column] == '1' and not flag[row - 1][column]:
            self.__dfs__(grid, row - 1, column, flag)


s = Solution()
grid = [["1"], ["1"]]

print(s.numIslands(grid))
