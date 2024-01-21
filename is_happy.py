# https://leetcode.cn/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def isHappy(self, n: int) -> bool:
        for _ in range(100):
            n = self.convert(n)
            if n == 1:
                return True
        return False

    def convert(self, num: int) -> int:
        result = 0
        while num > 0:
            result += (num % 10) ** 2
            num //= 10
        return result


s = Solution()
print(s.isHappy(2))

# 此题的正确解法应该是判断结果正否存在循环，当为1时不存在循环，否则会存在循环。而不是以100次为标准
# 参考： https://leetcode.cn/problems/happy-number/solutions/224894/kuai-le-shu-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150

