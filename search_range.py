# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List

class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos, last_pos = -1, -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                i = mid - 1
                while i >= 0 and nums[i] == target:
                    i -= 1
                first_pos = i + 1

                j = mid + 1
                while j < len(nums) and nums[j] == target:
                    j += 1
                last_pos = j - 1

                break

        return [first_pos, last_pos]

s = Solution()
nums = [1,1,2]
target = 1

result = s.searchRange(nums, target)
print(result)


