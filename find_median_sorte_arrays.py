# https://leetcode.cn/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.get_kth(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1)
        else:
            mid1 = self.get_kth(nums1, nums2, (len(nums1) + len(nums2)) // 2)
            mid2 = self.get_kth(nums1, nums2, (len(nums1) + len(nums2)) // 2 + 1)
            return (mid1 + mid2) / 2

    # 获取两个list中排名第k的数字
    def get_kth(self, list1, list2, k):
        skip_number = k - 1   # 获取排名第k的数字，就是要skip掉前面k-1的数字
        p1, p2 = 0, 0

        while skip_number > 0 and p1 < len(list1) and p2 < len(list2):
            if list1[p1] >= list2[p2]:
                p2 += 1
            else:
                p1 += 1
            skip_number -= 1

        if p1 < len(list1) and p2 < len(list2):
            return min(list1[p1], list2[p2])

        if p1 == len(list1):
            p1 = p2
            list1 = list2

        return list1[p1 + skip_number]


s = Solution()

list1 = [1, 2]
list2 = [3, 4]
print(s.findMedianSortedArrays(list1, list2))