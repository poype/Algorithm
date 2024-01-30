# https://leetcode.cn/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False

        p = head
        q = head.next

        while q is not None and p != q:
            p = p.next
            q = q.next
            if q is None:
                return False
            q = q.next

        if q is None:
            return False

        return True
