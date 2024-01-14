# https://leetcode.cn/problems/product-of-array-except-self/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product_list, right_product_list = [1], [1]
        n = len(nums)
        left_product = 1
        right_product = 1

        for i in range(1, n):
            left_product = left_product * nums[i - 1]
            left_product_list.append(left_product)

        for i in range(n - 2, -1, -1):
            right_product = right_product * nums[i + 1]
            right_product_list.insert(0, right_product)

        result = []
        for i in range(n):
            result.append(left_product_list[i] * right_product_list[i])

        return result


s = Solution()
l = [-1,1,0,-3,3]

print(s.productExceptSelf(l))
