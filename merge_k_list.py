# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        q = head
        p = self.pointer_of_minium(lists)

        while p is not None:
            q.next = p
            q = p
            p = self.pointer_of_minium(lists)

        return head.next

    def pointer_of_minium(self, lists: List[ListNode]) -> ListNode | None:
        min_value = 2 ** 32 - 1
        index = -1
        for i in range(len(lists)):
            if lists[i] is not None and lists[i].val < min_value:
                min_value = lists[i].val
                index = i

        if index == -1:
            return None

        p = lists[index]
        lists[index] = p.next
        return p


s = Solution()

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

la1 = ListNode(1)
la2 = ListNode(4)
la3 = ListNode(5)
la1.next = la2
la2.next = la3

lb1 = ListNode(1)
lb2 = ListNode(3)
lb3 = ListNode(4)
lb1.next = lb2
lb2.next = lb3

lc1 = ListNode(2)
lc2 = ListNode(6)
lc1.next = lc2

head = s.mergeKLists([la1, lb1, lc1])
print(head)
