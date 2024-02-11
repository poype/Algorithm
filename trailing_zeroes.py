# https://leetcode.cn/problems/factorial-trailing-zeroes/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 1
        while n > 0:
            result *= n
            n -= 1

        zero_cnt = 0
        mod_val = result % 10
        while mod_val == 0:
            zero_cnt += 1
            result = result // 10
            mod_val = result % 10

        return zero_cnt


s = Solution()
print(s.trailingZeroes(3))


# Time Limit，只需要考虑2和5因子的个数就行
