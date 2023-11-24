# https://leetcode.cn/problems/longest-valid-parentheses/

class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        # table中的第i个元素记录的是字符串s中以第i个字符结尾的有效括号长度
        table = [0 for i in range(len(s))]

        longest = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                # 如果是(，那以i结尾的有效括号长度一定是0
                table[i] = 0
            else:
                if s[i - 1] == '(':
                    if i == 1:
                        table[i] = 2
                    else:
                        table[i] = 2 + table[i - 2]
                else:
                    pre_pos = i - table[i - 1] - 1
                    if pre_pos >= 0 and s[pre_pos] == '(':
                        if pre_pos >= 2 and s[pre_pos - 1] == ')':
                            # ()(()) 这种case
                            table[i] = table[i - 1] + 2 + table[pre_pos - 1]
                        else:
                            table[i] = table[i - 1] + 2
                    else:
                        table[i] = 0

            if table[i] > longest:
                longest = table[i]

        return longest



s = Solution()

print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses(")(((((()())()()))()(()))("))
print(s.longestValidParentheses(""))

