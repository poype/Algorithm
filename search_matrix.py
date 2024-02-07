# https://leetcode.cn/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            row = matrix[i]
            if row[0] >= target:
                break
            i += 1

        if i == 0:
            if matrix[0][0] == target:
                return True
            return False

        if i < len(matrix) and matrix[i][0] == target:
            return True

        row = matrix[i - 1]
        if target in row:
            return True
        return False


s = Solution()
matrix = [[1], [3]]
target = 3

print(s.searchMatrix(matrix, target))
