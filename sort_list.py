# https://leetcode.cn/problems/sort-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        head_head = ListNode()
        head_head.next = head
        o = head
        p = head.next

        max_val = head.val

        while p is not None:
            q = p.next

            if p.val >= max_val:
                max_val = p.val
                o = p
            else:
                m, n = head_head, head_head.next
                while n.val < p.val:
                    m = m.next
                    n = n.next
                o.next = q
                p.next = n
                m.next = p
            p = q
        return head_head.next
