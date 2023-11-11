# https://leetcode.cn/problems/palindrome-number/

class Solution(object):

    def isPalindrome(self, num):

        if num < 0:
            return False

        num_copy = num

        result = 0
        while num > 0:
            result = result * 10 + num % 10
            num = num // 10

        return num_copy == result


s = Solution()
print(s.isPalindrome(123))
