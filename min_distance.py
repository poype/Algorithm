# https://leetcode.cn/problems/edit-distance/?envType=study-plan-v2&envId=top-interview-150
from typing import Dict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        此题中描述包括插入一个字符、删除一个字符、替换一个字符三种操作，但删除和插入本质上属于同一种操作
        所以只需要考虑删除、替换两种操作即可
        """
        cache = {}
        return self.__min_distance__(word1, word2, cache)

    def __min_distance__(self, word1: str, word2: str, cache: Dict) -> int:
        l1, l2 = len(word1), len(word2)

        if l1 == 0:
            return l2
        if l2 == 0:
            return l1

        if f"{word1}_{word2}" in cache:
            return cache[f"{word1}_{word2}"]

        if word1[l1 - 1] == word2[l2 - 1]:
            cache[f"{word1}_{word2}"] = self.__min_distance__(word1[:l1 - 1], word2[:l2 - 1], cache)
        else:
            cache[f"{word1}_{word2}"] = 1 + min(self.__min_distance__(word1[:l1 - 1], word2[:l2 - 1], cache),
                                                self.__min_distance__(word1[:l1 - 1], word2, cache),
                                                self.__min_distance__(word1, word2[:l2 - 1], cache))
        return cache[f"{word1}_{word2}"]


s = Solution()
word1 = "dinitrophenylhydrazine"
word2 = "benzalphenylhydrazone"
print(s.minDistance(word1, word2))
