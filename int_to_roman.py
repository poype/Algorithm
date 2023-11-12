# https://leetcode.cn/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        d = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        result = ''
        for key in d.keys():
            count = num // key
            result = result + (d.get(key) * count)  # 字符串类型也可以参与乘法运算
            num %= key

        return result


s = Solution()
result = s.intToRoman(1994)
print(result)
