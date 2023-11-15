# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        p, q = head, head
        i = 0
        while i < n + 1:
            q = q.next
            i += 1
            if q is None:
                break

        # 这种情况，一定是删除链表的第一个节点
        if i < (n + 1):
            return head.next

        while q is not None:
            q = q.next
            p = p.next

        o = p.next
        p.next = o.next
        o.next = None

        return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
head = s.removeNthFromEnd(l1, 2)

print(head)
