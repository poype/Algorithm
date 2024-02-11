# https://leetcode.cn/problems/word-break/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag_list = [None for _ in range(len(s))]
        return self.__word_break__(s, wordDict, 0, flag_list)

    def __word_break__(self, s: str, wordDict: List[str], start: int, flag_list: list[Optional[bool]]) -> bool:
        if start == len(s):
            return True

        if flag_list[start] is not None:
            return flag_list[start]

        if start == len(s):
            flag_list[start] = True
            return True

        for word in wordDict:
            if s.startswith(word, start, len(s)) and self.__word_break__(s, wordDict, start + len(word), flag_list):
                flag_list[start] = True
                return True

        flag_list[start] = False
        return False


solution = Solution()
s = "leetcode"
wordDict = ["leet", "code"]

print(solution.wordBreak(s, wordDict))