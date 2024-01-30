# https://leetcode.cn/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def __init__(self):
        self.num_chs = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    def calculate(self, s: str) -> int:
        stack = []
        self.extract_word(s, stack)
        if stack[0] == '-':
            return -stack[1]
        return stack[0]

    def extract_word(self, remain_s: str, stack: List):
        remain_s = remain_s.lstrip()
        if len(remain_s) > 0:
            if remain_s[0] == '(' or remain_s[0] == '+' or remain_s[0] == '-':
                stack.append(remain_s[0])
                self.extract_word(remain_s[1:], stack)
            elif remain_s[0] in self.num_chs:
                i = 1
                while i < len(remain_s) and remain_s[i] in self.num_chs:
                    i += 1
                num = int(remain_s[0: i])
                if len(stack) > 0 and stack[len(stack) - 1] == '+':
                    stack.pop()
                    num2 = stack.pop()
                    stack.append(num + num2)
                elif len(stack) > 0 and stack[len(stack) - 1] == '-':
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(-num)
                    elif stack[len(stack) - 1] == '(':
                        stack.pop()
                        stack.append(-num)
                        while remain_s[i] != ')':
                            i += 1
                        i += 1

                        while len(stack) > 2 and (stack[len(stack) - 2] == '+' or stack[len(stack) - 2] == '-'):
                            num1 = stack.pop()
                            op = stack.pop()
                            num2 = stack.pop()
                            if op == '+':
                                stack.append(num2 + num1)
                            elif op == '-':
                                stack.append(num2 - num1)

                        if len(stack) == 2 and stack[0] == '-':
                            num = stack.pop()
                            stack.pop()
                            stack.append(-num)
                    else:
                        num2 = stack.pop()
                        stack.append(num2 - num)
                else:
                    stack.append(num)
                self.extract_word(remain_s[i:], stack)
            elif remain_s[0] == ')':
                num = stack.pop()
                stack.pop()
                stack.append(num)
                while len(stack) > 2 and (stack[len(stack) - 2] == '+' or stack[len(stack) - 2] == '-'):
                    num1 = stack.pop()
                    op = stack.pop()
                    num2 = stack.pop()
                    if op == '+':
                        stack.append(num2 + num1)
                    elif op == '-':
                        stack.append(num2 - num1)

                if len(stack) == 2 and stack[0] == '-':
                    num = stack.pop()
                    stack.pop()
                    stack.append(-num)

                self.extract_word(remain_s[1:], stack)


s = Solution()
exp = "- (3 - (- (4 + 5) ) )"
print(s.calculate(exp))
