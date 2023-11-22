# https://leetcode.cn/problems/divide-two-integers/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor

        flag = False
        if dividend < 0:
            dividend = -dividend
            flag = True

        if divisor < 0:
            divisor = -divisor
            flag = True

        count = 0

        if divisor == 1:
            count = dividend
        else:
            while dividend >= divisor:
                dividend -= divisor
                count += 1

        if flag:
            count = -count

        if count > 2 ** 31 - 1:
            count = 2 ** 31 - 1

        if count < -(2 ** 31):
            count = -(2 ** 31)

        return count


s = Solution()
result = s.divide(10, 3)
print(result)

num = 10

print(num << 1)  # 20 左移一位相当于乘以2
print(num >> 1)  # 5  右移一位相当于除以2

print(num >> 1)
