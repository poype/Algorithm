# https://leetcode.cn/problems/multiply-strings/


# python 数字与字符串之间的类型转换非常简单
class Solution(object):
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


s = Solution()

print(s.multiply("2", "3"))
