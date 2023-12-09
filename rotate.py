# https://leetcode.cn/problems/rotate-image/

from typing import List

class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            for o in range(i, n - i - 1):
                t = matrix[i][i]
                for j in range(i, n - i - 1):
                    t, matrix[i][j + 1] = matrix[i][j + 1], t
                for k in range(i, n - i - 1):
                    t, matrix[k + 1][n - i - 1] = matrix[k + 1][n - i - 1], t
                for l in range(n - i - 1, i, -1):
                    t, matrix[n - i - 1][l - 1] = matrix[n - i - 1][l - 1], t
                for m in range(n - i - 1, i, -1):
                    t, matrix[m - 1][i] = matrix[m - 1][i], t

s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)

# 就是简单的移动元素，只是数组下表计算有点烦
# 值得注意的是 for m in range(n - i - 1, i, -1) 逆序遍历
