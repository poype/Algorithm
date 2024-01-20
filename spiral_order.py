# https://leetcode.cn/problems/spiral-matrix/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        result = []

        while top <= bottom and left <= right:
            # 从左到右遍历上边界
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 从右到左遍历下边界
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

                # 从下到上遍历左边界
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
s = Solution()
print(s.spiralOrder(matrix))
