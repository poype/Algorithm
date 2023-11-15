# https://leetcode.cn/problems/valid-parentheses/


class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif len(stack) == 0:  # 如果stack是空的，pop时会抛异常
                return False
            elif s[i] == ')':
                ch = stack.pop()
                if ch != '(':
                    return False
            elif s[i] == ']':
                ch = stack.pop()
                if ch != '[':
                    return False
            elif s[i] == '}':
                ch = stack.pop()
                if ch != '{':
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid("(]"))



