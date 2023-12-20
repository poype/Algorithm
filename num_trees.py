# https://leetcode.cn/problems/unique-binary-search-trees/
# 应该是要计算 有序二叉树 的数量

from typing import List

class Solution:
    def __init__(self):
        self.cache = {}

    def numTrees(self, n: int) -> int:
        arr = []
        for i in range(1, n + 1):   # 此题入参只有一个数字n，将n转为数组
            arr.append(i)

        sum = 0
        for i in range(n):
            sum += self.create_order_tree(arr[i], arr[:i], arr[i + 1:])
        return sum

    # 该方法计算以某个节点为局部root时子树的数量
    def create_order_tree(self, root: int, left_list: List[int], right_list: List[int]) -> int:
        # 使用join()函数将数字列表转换为一个字符串
        left_list_string = ''.join(map(str, left_list))
        right_list_string = ''.join(map(str, right_list))
        key = f"{left_list_string}-{root}-{right_list_string}"
        if self.cache.__contains__(key):
            return self.cache[key]

        left_sum, right_sum = 0, 0
        if len(left_list) > 1:
            for i in range(len(left_list)):
                left_sum += self.create_order_tree(left_list[i], left_list[:i], left_list[i + 1:])

        if len(right_list) > 1:
            for i in range(len(right_list)):
                right_sum += self.create_order_tree(right_list[i], right_list[:i], right_list[i + 1:])

        if left_sum == 0:
            left_sum = 1  # 之所以设置成1，因为即使左子树为空，也应该算是一种case
        if right_sum == 0:
            right_sum = 1

        self.cache[key] = left_sum * right_sum
        return left_sum * right_sum


s = Solution()
print(s.numTrees(19))
