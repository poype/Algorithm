# https://leetcode.cn/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        carry = (digits[n - 1] + 1) // 10
        digits[n - 1] = (digits[n - 1] + 1) % 10
        for i in range(n - 2, -1, -1):
            if carry == 0:
                break
            temp_carry = (digits[i] + carry) // 10
            digits[i] = (digits[i] + carry) % 10
            carry = temp_carry

        if carry > 0:
            digits.insert(0, carry)

        return digits


digits = [9, 9]
s = Solution()
print(s.plusOne(digits))
