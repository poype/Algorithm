# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        head_head = ListNode()
        head_head.next = head

        i = head_head
        j = head
        k = head.next

        while k is not None:
            if j.val != k.val:
                i = j
                j = k
                k = k.next
                continue

            while k is not None and j.val == k.val:
                k = k.next

            i.next = k
            if k is not None:
                j = k
                k = k.next

        return head_head.next


s = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

l = s.deleteDuplicates(node1)

print()
