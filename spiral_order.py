# https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        row_num = len(matrix)
        column_num = len(matrix[0])

        if column_num == 1:
            for r in range(row_num):
                result.append(matrix[r][0])
            return result

        if row_num == 1:
            for c in range(column_num):
                result.append(matrix[0][c])
            return result

        n = min(row_num, column_num) // 2

        for i in range(n):
            for c in range(i, column_num - i - 1):
                result.append(matrix[i][c])

            for r in range(i, row_num - i - 1):
                result.append(matrix[r][column_num - i - 1])

            for c in range(column_num - i - 1, i, -1):
                result.append(matrix[row_num - 1 - i][c])

            for r in range(row_num - 1 - i, i, -1):
                result.append(matrix[r][i])

        if min(row_num, column_num) % 2 == 1:
            if row_num < column_num:
                r = row_num // 2
                for c in range(r, column_num - r):
                    result.append(matrix[r][c])
            else:
                c = column_num // 2
                for r in range(c, row_num - c):
                    result.append(matrix[r][c])

        return result

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
s = Solution()
print(s.spiralOrder(matrix))
