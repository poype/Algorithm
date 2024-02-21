# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import List


class Solution(object):

    def __init__(self):
        self.num_char_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def letterCombinations(self, digits: str) -> List[str]:
        return self.convertToChar(digits, 0)

    def convertToChar(self, digits: str, start_pos: int) -> List[str]:
        result = []

        if len(digits) == 0:
            return result

        if start_pos == len(digits) - 1:
            return self.num_char_map[digits[start_pos]]

        sub_str_list = self.convertToChar(digits, start_pos + 1)
        char_array = self.num_char_map[digits[start_pos]]

        for i in range(len(char_array)):
            for j in range(len(sub_str_list)):
                result.append(char_array[i] + sub_str_list[j])

        return result


s = Solution()
digits = "2"

print(s.letterCombinations(digits))
