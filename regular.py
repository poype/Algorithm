# https://leetcode.cn/problems/regular-expression-matching/

class Solution(object):
    def __init__(self):
        self.dp = None
    def isMatch(self, s, p):
        # 这里注意矩阵的大小，要用len(p) + 1 和 len(s) + 1
        # 还要注意矩阵的方向不要搞反
        self.dp = [[None for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        return self.is_match(s, p, 0, 0)

    def is_match(self, s, p, i, j):
        if self.dp[i][j] is not None:
            return self.dp[i][j]

        if i == len(s) and j == len(p):
            self.dp[i][j] = True
            return True

        if i < len(s) and j == len(p):
            self.dp[i][j] = False
            return False

        if i == len(s) and (j + 1 >= len(p) or p[j + 1] != '*'):
            self.dp[i][j] = False
            return False

        if j + 1 < len(p) and p[j + 1] == '*':
            if i == len(s) or (s[i] != p[j] and p[j] != '.'):
                return self.is_match(s, p, i, j + 2)
            else:
                return (self.is_match(s, p, i, j + 2) or
                        self.is_match(s, p, i + 1, j + 2) or
                        self.is_match(s, p, i + 1, j))

        if s[i] == p[j] or p[j] == '.':
            return self.is_match(s, p, i + 1, j + 1)
        else:
            self.dp[i][j] = False
            return False


s = Solution()
print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*c"))
