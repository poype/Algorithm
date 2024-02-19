# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0

        # 子字符串的开始和结束指针
        start, end = 0, 1
        longest = 1
        unique_set = set()
        unique_set.add(s[0])

        while end != len(s):
            if s[end] not in unique_set:
                unique_set.add(s[end])
                if end - start + 1 > longest:
                    longest = end - start + 1
                end += 1
            else:
                while s[start] != s[end]:
                    unique_set.remove(s[start])
                    start += 1

                unique_set.remove(s[start])
                start += 1

        return longest


s = Solution()
print(s.lengthOfLongestSubstring(""))

