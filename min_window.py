# https://leetcode.cn/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def __init__(self):
        # key是字符，value是该字符的数量
        self.s_ch_cnt = {}
        self.t_ch_cnt = {}

    def minWindow(self, s: str, t: str) -> str:
        s_n, t_n = len(s), len(t)
        start, end = 0, t_n
        self.init_ch_cnt_dict(s[start: end], t)

        if s_n == t_n and self.contain_all_chars():
            return s

        min_len = s_n + 1
        min_s = ""
        for start in range(0, s_n - t_n + 1):
            if self.contain_all_chars():
                if end - start < min_len :
                    min_len = end - start
                    min_s = s[start: end]
                self.s_ch_cnt[s[start]] -= 1
                continue

            while end < s_n:
                self.add_ch_to_s_dict(s[end])
                end += 1
                if self.contain_all_chars():
                    if end - start < min_len:
                        min_len = end - start
                        min_s = s[start: end]
                    break

            self.s_ch_cnt[s[start]] -= 1
        return min_s

    def add_ch_to_s_dict(self, ch):
        if ch not in self.s_ch_cnt:
            self.s_ch_cnt[ch] = 0
        self.s_ch_cnt[ch] += 1

    def init_ch_cnt_dict(self, s: str, t: str):
        s_n = len(s)
        t_n = len(t)

        for i in range(s_n):
            if s[i] not in self.s_ch_cnt:
                self.s_ch_cnt[s[i]] = 0
            self.s_ch_cnt[s[i]] += 1

        for i in range(t_n):
            if t[i] not in self.t_ch_cnt:
                self.t_ch_cnt[t[i]] = 0
            self.t_ch_cnt[t[i]] += 1

    def contain_all_chars(self):
        """
        :return: s字符串中包含t字符串中的所有字符返回True，否则返回False
        """
        for t_key in self.t_ch_cnt.keys():
            if t_key not in self.s_ch_cnt:
                return False

            if self. s_ch_cnt[t_key] < self.t_ch_cnt[t_key]:
                return False

        return True


solution = Solution()
s = "a"
t = "a"
print(solution.minWindow(s, t))