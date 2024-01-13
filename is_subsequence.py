# https://leetcode.cn/problems/is-subsequence/description/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        sn, tn = len(s), len(t)
        while si < sn and ti < tn:
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1

        return si == sn


s = Solution()
print(s.isSubsequence("axc", "ahbgdc"))