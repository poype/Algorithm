# https://leetcode.cn/problems/generate-parentheses/

from typing import List


class Solution(object):
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_parenthesis(n, n)

    def generate_parenthesis(self, n: int, m: int) -> List[str]:
        """
        :param n: 括号剩余的数量
        :param m: 括回剩余的数量
        采用分治法的思想，如果整个字符串的长度是N，那么先计算前N-1字符串的所有组合，再通过条件判断第N位是用括号还是括回即可。
        n 一定小于等于 m
        """
        if n == 0 and m == 1:
            return [')']

        result = []
        if n == m:
            sub_str_list = self.generate_parenthesis(n - 1, m)
            for i in range(len(sub_str_list)):
                result.append("(" + sub_str_list[i])
        elif n == 0:
            sub_str_list = self.generate_parenthesis(n, m - 1)
            for i in range(len(sub_str_list)):
                result.append(")" + sub_str_list[i])
        else:  # n < m
            sub_str_list = self.generate_parenthesis(n - 1, m)
            for i in range(len(sub_str_list)):
                result.append("(" + sub_str_list[i])

            sub_str_list = self.generate_parenthesis(n, m - 1)
            for i in range(len(sub_str_list)):
                result.append(")" + sub_str_list[i])

        return result


s = Solution()

print(s.generateParenthesis(1))
