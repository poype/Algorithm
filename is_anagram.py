# https://leetcode.cn/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 0
            s_dict[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 0
            t_dict[t[i]] += 1

        for key in s_dict.keys():
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False

        return True


