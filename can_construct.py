# https://leetcode.cn/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # key是字符，value是字符出现的次数
        r_dict = {}
        m_dict = {}

        for i in range(len(ransomNote)):
            if ransomNote[i] not in r_dict:
                r_dict[ransomNote[i]] = 0
            r_dict[ransomNote[i]] += 1

        for i in range(len(magazine)):
            if magazine[i] not in m_dict:
                m_dict[magazine[i]] = 0
            m_dict[magazine[i]] += 1

        for ch in r_dict:
            if ch not in m_dict or r_dict[ch] > m_dict[ch]:
                return False

        return True


s = Solution()
ransomNote = "a"
magazine = "ba"
print(s.canConstruct(ransomNote, magazine))
