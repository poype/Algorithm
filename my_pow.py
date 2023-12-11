# https://leetcode.cn/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag = False
        if n < 0:
            n = -n
            flag = True

        result = 1.0

        for i in range(n):
            result = result * x

        if flag:
            return 1 / result
        return result


s = Solution()
print(s.myPow(2.00000, -2))