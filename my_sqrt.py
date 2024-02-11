# https://leetcode.cn/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def mySqrt(self, x: int) -> int:
        x = x ** 0.5
        return int(x)


s = Solution()
print(s.mySqrt(8))
