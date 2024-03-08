# https://leetcode.cn/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head

        p = head_head
        q = head
        while q is not None and q.val < x:
            p = p.next
            q = q.next

        if q is None:
            return head_head.next

        i, j = q, q.next
        while j is not None:
            if j.val < x:
                i.next = j.next
                j.next = p.next
                p.next = j
                p = p.next
                j = i.next
            else:
                j = j.next
                i = i.next

        return head_head.next


