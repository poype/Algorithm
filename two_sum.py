# https://leetcode.cn/problems/two-sum/description/

class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # key is number, value is index
        index_dict = dict()

        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in index_dict:
                return [index_dict[num2], i]

            index_dict[nums[i]] = i


# test
nums = [3, 2, 4]
target = 6

s = Solution()

result = s.two_sum(nums, target)
print(result)
