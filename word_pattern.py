# https://leetcode.cn/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(" ")
        if len(word_list) != len(pattern):
            return False

        map = {}
        mapped = set()
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if word_list[i] in mapped:
                    return False

                map[pattern[i]] = word_list[i]
                mapped.add(word_list[i])

            if map[pattern[i]] != word_list[i]:
                return False

        return True