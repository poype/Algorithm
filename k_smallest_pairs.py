# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
from typing import List
import heapq


class Pair:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def __lt__(self, other: 'Pair'):
        return (self.num1 + self.num2) > (other.num1 + other.num2)

    def convert(self):
        return [self.num1, self.num2]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        heap_queue = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(heap_queue, Pair(nums1[i], nums2[j]))
                if len(heap_queue) > k:
                    heapq.heappop(heap_queue)

        for _ in range(k):
            if len(heap_queue) == 0:
                break
            result.append(heapq.heappop(heap_queue).convert())

        return result


s = Solution()
nums1 = [1, 2]
nums2 = [3]
k = 3
print(s.kSmallestPairs(nums1, nums2, k))
