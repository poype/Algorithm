# https://leetcode.cn/problems/minimum-path-sum/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
        return self.__walk__(grid, 0, 0, cache)

    def __walk__(self, grid: List[List[int]], row: int, column: int, cache: List[List[int]]) -> int:
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return grid[row][column]

        if cache[row][column] is not None:
            return cache[row][column]

        val_below, val_right = 2 ** 32, 2 ** 32
        if row < len(grid) - 1:
            val_below = self.__walk__(grid, row + 1, column, cache)

        if column < len(grid[0]) - 1:
            val_right = self.__walk__(grid, row, column + 1, cache)

        cache[row][column] = grid[row][column] + min(val_right, val_below)
        return grid[row][column] + min(val_right, val_below)


s = Solution()
grid = [[1, 2, 3], [4, 5, 6]]

print(s.minPathSum(grid))
