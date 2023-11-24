# https://leetcode.cn/problems/next-permutation/

from typing import List


class Solution(object):
    def nextPermutation(self, nums: List[int]) -> None:
        if not self.next_permutation(nums, 0):
            nums.sort()

    def next_permutation(self, nums: List[int], start: int) -> bool:
        if start == len(nums) - 1:
            return False

        if start == len(nums) - 2:
            if nums[start] < nums[start + 1]:
                nums[start], nums[start + 1] = nums[start + 1], nums[start]
                return True
            else:
                return False

        if self.next_permutation(nums, start + 1):
            return True

        if nums[start] > nums[start + 1]:
            return False

        p = len(nums) - 1
        while p > start:
            if nums[p] > nums[start]:
                break
            p -= 1

        if p == start:
            return False  # 没找到大的值

        nums[start], nums[p] = nums[p], nums[start]

        # start后面的元素按正向排序
        i = start + 1
        j = len(nums) - 1
        while j > i:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return True


nums = [1, 3, 2]
solution = Solution()

solution.nextPermutation(nums)

print(nums)
