# https://leetcode.cn/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        flag = False

        if x < 0:
            flag = True
            x = -x

        result = 0

        while x > 0:
            result = result * 10 + x % 10
            x = x // 10

        if flag:
            result = -result

        max32 = 2 ** 31 - 1
        min32 = -(2 ** 31)
        if result > max32 or result < min32:
            return 0
        return result


s = Solution()
print(s.reverse(-123))


