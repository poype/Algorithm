# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# find 和 index 两个方法的区别：
# 如果主字符串中不包含对应的子字符串，find方法会返回-1，index方法会抛异常


s = Solution()
print(s.strStr("leetcode", "leeto"))
