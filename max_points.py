# https://leetcode.cn/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        max_cnt = 2
        for i in range(n - 1):
            for j in range(i + 1, n):
                cnt = 2
                if points[i][0] == points[j][0]:
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if points[k][0] == points[i][0]:
                            cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt

                elif points[i][1] == points[j][1]:
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if points[k][1] == points[i][1]:
                            cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt

                else:
                    exp = self.__expression__(points[i], points[j])
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if points[k][1] == points[k][0] * exp[0] + exp[1]:
                            cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
        return max_cnt

    def __expression__(self, point1: List[int], point2: List[int]) -> List[float]:
        if point1[0] == point2[0]:
            return [0, ]

        m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        n = point2[1] - (m * point2[0])
        return [m, n]


s = Solution()
points = [[1,1],[2,2],[3,3]]
print(s.maxPoints(points))



print(0.5 * 2 == 1)  # True  Python中可以很好的处理float数的精度

