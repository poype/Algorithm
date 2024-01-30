# https://leetcode.cn/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif ch == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif ch == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif ch == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                quotient = abs(num2) // abs(num1)       # 注意商的英文单词
                if num1 < 0 < num2 or num2 < 0 < num1:  # 注意这种写法
                    quotient = -quotient
                stack.append(quotient)
            else:
                stack.append(int(ch))

        return stack[0]


s = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(s.evalRPN(tokens))


