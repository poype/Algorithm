# https://leetcode.cn/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)

        if n == 0:
            return 0

        start, end = 0, 0
        last_word = ""
        for i in range(len(s)):
            if s[i] == " ":
                end = i - 1
                last_word = s[start: end + 1]
                start = i + 1
            elif i == n - 1:
                last_word = s[start: n]

        return len(last_word)

s = Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))
