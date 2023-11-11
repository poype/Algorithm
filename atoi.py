# https://leetcode.cn/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0:
            return 0

        map = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }

        flag = False
        if s[0] == '+' and len(s) > 1:
            s = s[1:]
        elif s[0] == '+':
            return 0
        elif s[0] == '-' and len(s) > 1:
            flag = True
            s = s[1:]
        elif s[0] == '-':
            return 0

        result, i = 0, 0
        while i < len(s):
            num = map.get(s[i])
            if num == None:
                break

            result = result * 10 + num
            i += 1

        if flag:
            result = -result

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -(2 ** 31):
            return -(2 ** 31)

        return result

s = Solution()
print(s.myAtoi(""))
