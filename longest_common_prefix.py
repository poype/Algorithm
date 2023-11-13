# https://leetcode.cn/problems/longest-common-prefix/
from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""

        i = 0
        result = ""
        while True:
            if i >= len(strs[0]):
                return result

            for k in range(1, len(strs)):
                if i >= len(strs[k]) or strs[0][i] != strs[k][i]:
                    return result

            # 字符串类型可以数字一样使用“+”符号
            result += strs[0][i]
            i += 1


s = Solution()
strs = ["a"]

print(s.longestCommonPrefix(strs))
