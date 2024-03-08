# https://leetcode.cn/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head

        cnt = 0
        p = head
        while p is not None:
            cnt += 1
            p = p.next

        if cnt == 0:
            return None

        k = k % cnt
        if k == 0:
            return head

        p, q = head_head, head
        for _ in range(1, k):
            q = q.next

        while q.next is not None:
            q = q.next
            p = p.next

        q.next = head_head.next
        head_head.next = p.next
        p.next = None

        return head_head.next


s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5

l = s.rotateRight(None, 0)

print(l)

