# https://leetcode.cn/problems/regular-expression-matching/

class Solution(object):
    def isMatch(self, s, p):
        return self.is_match(s, p, 0, 0)

    def is_match(self, s, p, i, j):
        if i == len(s) and j == len(p):
            return True

        if i < len(s) and j == len(p):
            return False

        if i == len(s) and (j + 1 >= len(p) or p[j + 1] != '*'):
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
            return False


s = Solution()
print(s.isMatch("ab", ".*c"))
