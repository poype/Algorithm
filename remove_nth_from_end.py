# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int):
        head_head = ListNode()
        head_head.next = head

        cnt = 0
        p = head

        while p is not None:
            p = p.next
            cnt += 1

        cnt = cnt - n

        p = head_head
        for _ in range(cnt):
            p = p.next
        p.next = p.next.next
        return head_head.next


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
