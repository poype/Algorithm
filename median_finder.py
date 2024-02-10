# https://leetcode.cn/problems/find-median-from-data-stream/?envType=study-plan-v2&envId=top-interview-150
import heapq


class MedianFinder:
    def __init__(self):
        self.queue = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.queue, num)

    def findMedian(self) -> float:
        temp_queue = self.queue[:]

        n = len(temp_queue)

        pop_cnt = n // 2
        if n % 2 == 0:
            pop_cnt -= 1

        while pop_cnt > 0:
            heapq.heappop(temp_queue)
            pop_cnt -= 1

        if n % 2 == 1:
            val = heapq.heappop(temp_queue)
            return val
        else:
            val1 = heapq.heappop(temp_queue)
            val2 = heapq.heappop(temp_queue)
            return (val1 + val2) / 2


h = MedianFinder()
h.addNum(1)
h.addNum(2)
print(h.findMedian())
h.addNum(3)
print(h.findMedian())
