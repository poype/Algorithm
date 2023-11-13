# https://leetcode.cn/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        d = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        result = 0
        for roman in d.keys():
            while s.startswith(roman):
                result += d.get(roman)
                s = s.removeprefix(roman)

        return result


s = Solution()
print(s.romanToInt("MCMXCIV"))

