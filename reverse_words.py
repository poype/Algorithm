# https://leetcode.cn/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        n = len(s)
        if n == 0:
            return ""
        elif n == 1:
            return s

        start, end = 0, 0  # 一个单词的开始和结尾
        stack = []

        for i in range(1, n):
            if s[start] == " ":
                start = i + 1
                continue

            if s[i] == " ":
                end = i - 1
                word = s[start: end + 1]
                stack.append(word)
                start = i + 1
            elif i == n - 1:
                word = s[start: n]
                stack.append(word)

        result = ""
        while len(stack) > 0:
            word = stack.pop()
            result = result + word + " "

        return result.rstrip()

s = Solution()
print(s.reverseWords("F R  I   E    N     D      S      "))



