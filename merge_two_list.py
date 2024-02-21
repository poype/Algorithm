# https://leetcode.cn/problems/merge-two-sorted-lists/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p1, p2 = list1, list2
        head = ListNode()
        p = head

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next

        if p1 is None:
            p1 = p2

        p.next = p1

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
