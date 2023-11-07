# https://leetcode.cn/problems/longest-palindromic-substring/

class Solution(object):
    def __init__(self):
        self.longest = 1
        self.result = None

    def longestPalindrome(self, s):
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        self.result = s[0]

        # 记住这个在矩阵中走斜线的代码
        for k in range(len(s)):
            for i, j in zip(range(len(s) - k), range(k, len(s))):
                if i == j:
                    dp[i][j] = True
                    continue

                if s[i] != s[j]:
                    dp[i][j] = False
                    continue

                if j - i == 1:
                    dp[i][j] = True
                    self.update_result(s, i, j)
                    continue

                dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j]:
                    self.update_result(s, i, j)

        return self.result

    def update_result(self, s, start, end):
        self.longest = end - start + 1
        self.result = s[start: end + 1]


s = Solution()

result = s.longestPalindrome("cbbd")
print(result)