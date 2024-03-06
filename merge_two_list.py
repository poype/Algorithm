# https://leetcode.cn/problems/merge-two-sorted-lists/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        p = head

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next

        if list1 is None:
            list1 = list2

        while list1 is not None:
            p.next = list1
            list1 = list1.next
            p = p.next

        return head.next


s = Solution()

l1a = ListNode(1)
l1b = ListNode(2)
l1c = ListNode(4)
l1a.next = l1b
l1b.next = l1c

l2a = ListNode(1)
l2b = ListNode(3)
l2c = ListNode(4)
l2a.next = l2b
l2b.next = l2c

head = s.mergeTwoLists(l1a, l2a)

print(head)
