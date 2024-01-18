# https://leetcode.cn/problems/valid-palindrome/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        s_copy_array = []

        for i in range(n):
            if s[i].isalpha():
                s_copy_array.append(s[i])

        s_copy = "".join(s_copy_array)

        n = len(s_copy)
        i = 0
        while i < n // 2:
            if s_copy[i] != s_copy[n - 1 - i]:
                return False
            i += 1

        return True


s = Solution()
result = s.isPalindrome("race a car")
print(result)

# 算通过吧，感觉测试用例有问题

