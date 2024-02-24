# https://leetcode.cn/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)

        if n == 0:
            return 0

        word_list = s.split(" ")
        return len(word_list[-1])


s = Solution()
print(s.lengthOfLastWord("luffy is still joyboy"))
