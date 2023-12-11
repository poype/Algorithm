# https://leetcode.cn/problems/climbing-stairs/

class Solution(object):
    def __init__(self):
        self.record = []

    def climbStairs(self, n: int) -> int:
        self.record = [-1 for i in range(n + 1)]

        return self.climb_stairs(n)


    def climb_stairs(self, n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        if self.record[n] == -1:
            self.record[n] = self.climb_stairs(n - 1) + self.climb_stairs(n - 2)

        return self.record[n]



s = Solution()
print(s.climbStairs(44))