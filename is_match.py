# https://leetcode.cn/problems/wildcard-matching/

class Solution(object):
    def isMatch(self, s: str, p: str) -> bool:
        return self.is_match(s, p, 0, 0)

    def is_match(self, s: str, p: str, s_cursor: int, p_cursor: int) -> bool:
        if s_cursor == len(s) and p_cursor == len(p):
            return True
        elif s_cursor == len(s) and p[p_cursor] == '*':
            return self.is_match(s, p, s_cursor, p_cursor+1)
        elif s_cursor == len(s) or p_cursor == len(p):
            return False

        if s[s_cursor] == p[p_cursor]:
            return self.is_match(s, p, s_cursor + 1, p_cursor + 1)
        elif p[p_cursor] == '?':
            return self.is_match(s, p, s_cursor + 1, p_cursor + 1)
        elif p[p_cursor] == '*':
            return (self.is_match(s, p, s_cursor + 1, p_cursor + 1) or
                    self.is_match(s, p, s_cursor, p_cursor + 1) or
                    self.is_match(s, p, s_cursor + 1, p_cursor))
        else:
            return False


s = Solution()
print(s.isMatch("aa", "a"))
print(s.isMatch("cb", "?a"))

