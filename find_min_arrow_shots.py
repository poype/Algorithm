# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        points.sort(key=lambda item: item[0])
        overlap_range = [points[0][0], points[0][1]]
        cnt = 1
        for i in range(1, len(points)):
            if overlap_range[0] <= points[i][1] and overlap_range[1] >= points[i][0]:
                overlap_range[0] = max(overlap_range[0], points[i][0])
                overlap_range[1] = min(overlap_range[1], points[i][1])
            else:
                overlap_range = [points[i][0], points[i][1]]
                cnt += 1
        return cnt


s = Solution()
points = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(s.findMinArrowShots(points))
