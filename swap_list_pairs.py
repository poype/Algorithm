# https://leetcode.cn/problems/swap-nodes-in-pairs/
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        p1 = head
        p2 = p1.next
        if p2 is None:
            return p1

        temp_head = ListNode()
        q = temp_head
        while p1 is not None and p2 is not None:
            next_p1 = p2.next
            if next_p1 is not None:
                next_p2 = next_p1.next
            else:
                next_p2 = None

            q.next = p2
            q = q.next
            q.next = p1
            q = q.next
            q.next = None

            p1 = next_p1
            p2 = next_p2

        q.next = p1

        return temp_head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

s = Solution()

result = s.swapPairs(l1)

print(result)
