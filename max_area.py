# https://leetcode.cn/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, heights):
        start, end = 0, len(heights) - 1
        max_area = 0
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            if area > max_area:
                max_area = area

            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return max_area


s = Solution()
heights = [1,8,6,2,5,4,8,3,7]

print(s.maxArea(heights))

