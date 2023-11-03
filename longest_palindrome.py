class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        """
        max_length = 0
        result = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if self.is_palindrome(s, i, j) and j - i + 1 > max_length:
                    max_length = j - i + 1
                    result = s[i: j + 1]

        return result

    def is_palindrome(self, s, start, end):
        """
        判断字符串s中的子序列是否是回文字符串
        :param s: 目标字符串
        :param start: 起始索引
        :param end: 终止索引
        :return: 回文字符串返回True，否则返回False
        """
        if start == end:
            return True
        elif start > end:
            return False

        if s[start] != s[end]:
            return False
        elif end - start == 1:
            return True
        else:
            return self.is_palindrome(s, start + 1, end - 1)


s = Solution()
print(s.longestPalindrome("abbbaddddddddddda"))
