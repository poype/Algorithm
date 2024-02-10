# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        n = len(nums)

        for i in range(n):
            heapq.heappush(queue, -nums[i])  # 注意这里要要负号

        for _ in range(1, k):
            heapq.heappop(queue)
        return -heapq.heappop(queue)


s = Solution()
l = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(s.findKthLargest(l, k))

# python中的heapq模块默认实现的是小顶堆，要想利用heapq实现大顶堆，可以参考这个doc
# https://blog.csdn.net/qq_32614873/article/details/128285500
