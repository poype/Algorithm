# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/

from builtins import str
from typing import List


# str类型的find方法和index方法的区别：当找不到子串时，find方法返回-1，index方法抛异常
# set类型的__len__方法计算集合的size，

class Solution(object):
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_count = len(words)
        sub_str_len = word_len * word_count

        result = []
        i = 0
        while len(s) - i >= sub_str_len:
            if self.is_match(s, words, i, word_len, word_count):
                result.append(i)
            i += 1

        return result

    def is_match(self, s: str, words: List[str], start: int, word_len: int, word_count: int) -> bool:
        index_set = set()
        while index_set.__len__() < word_count:
            end_flag = True
            for i in range(word_count):
                if s.find(words[i], start, start + word_len) != -1 and not index_set.__contains__(i):
                    index_set.add(i)
                    start += word_len
                    end_flag = False

            if end_flag:
                return False

        return True


solution = Solution()

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo", "barr", "wing", "ding", "wing"]

index_list = solution.findSubstring(s, words)
print(index_list)
