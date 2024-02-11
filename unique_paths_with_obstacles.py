# https://leetcode.cn/problems/unique-paths-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        return self.__walk__(obstacleGrid, 0, 0)

    def __walk__(self, grid: List[List[int]], row: int, column: int) -> int:
        if (row == len(grid) - 1 and column == len(grid[0]) - 1) and grid[len(grid) - 1][len(grid[0]) - 1] == 0:
            return 1

        if (((row + 1 == len(grid) - 1 and column == len(grid[0]) - 1) or
                (column + 1 == len(grid[0]) - 1) and row == len(grid) - 1) and
                grid[len(grid) - 1][len(grid[0]) - 1] == 0):
            return 1

        path_cnt = 0
        if row < len(grid) - 1 and grid[row + 1][column] == 0:
            path_cnt += self.__walk__(grid, row + 1, column)

        if column < len(grid[0]) - 1 and grid[row][column + 1] == 0:
            path_cnt += self.__walk__(grid, row, column + 1)

        return path_cnt


s = Solution()
obstacleGrid = [[0,0],[1,1],[0,0]]

print(s.uniquePathsWithObstacles(obstacleGrid))
