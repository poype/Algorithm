# https://leetcode.cn/problems/isomorphic-strings/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}
        mapped = set()

        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in mapped:
                    return False

                map[s[i]] = t[i]
                mapped.add(t[i])

            if map[s[i]] != t[i]:
                return False

        return True


s = "badc"
t = "baba"
solution = Solution()
result = solution.isIsomorphic(s, t)
print(result)