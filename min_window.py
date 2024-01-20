# https://leetcode.cn/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_n, t_n = len(s), len(t)
        if s_n == t_n and self.contain_all_chars(s, t):
            return s

        start, end = 0, t_n

        min_len = s_n + 1
        min_s = ""
        for start in range(0, s_n - t_n + 1):
            if self.contain_all_chars(s[start: end], t):
                if end - start < min_len :
                    min_len = end - start
                    min_s = s[start: end]
                continue

            while end < s_n:
                end += 1
                if self.contain_all_chars(s[start: end], t):
                    if end - start < min_len:
                        min_len = end - start
                        min_s = s[start: end]
                    break

        return min_s

    def contain_all_chars(self, s: str, t:str):
        """
        :return: s字符串中包含t字符串中的所有字符返回True，否则返回False
        """
        s_n = len(s)
        t_n = len(t)

        # key是字符，value是该字符的数量
        s_ch_cnt = {}
        t_ch_cnt = {}

        for i in range(s_n):
            if s[i] not in s_ch_cnt:
                s_ch_cnt[s[i]] = 0
            s_ch_cnt[s[i]] += 1

        for i in range(t_n):
            if t[i] not in t_ch_cnt:
                t_ch_cnt[t[i]] = 0
            t_ch_cnt[t[i]] += 1

        for t_key in t_ch_cnt.keys():
            if t_key not in s_ch_cnt:
                return False

            if s_ch_cnt[t_key] < t_ch_cnt[t_key]:
                return False

        return True


solution = Solution()
s = "abc"
t = "ac"
print(solution.minWindow(s, t))