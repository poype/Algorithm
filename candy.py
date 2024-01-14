# https://leetcode.cn/problems/candy/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy_list = [1 for _ in range(n)]

        while True:
            flag = False

            for i in range(n - 1):
                if ratings[i] > ratings[i + 1] and candy_list[i] <= candy_list[i + 1]:
                    flag = True
                    candy_list[i] = candy_list[i + 1] + 1

            for i in range(n - 1, 0, -1):
                if ratings[i] > ratings[i - 1] and candy_list[i] <= candy_list[i - 1]:
                    flag = True
                    candy_list[i] = candy_list[i - 1] + 1

            if not flag:
                break

        print(candy_list)
        return sum(candy_list)

s = Solution()
ratings = [29,51,87,87,72,12]
print(s.candy(ratings))

