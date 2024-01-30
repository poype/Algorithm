# https://leetcode.cn/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head  # 所有链表的操作，如果没有独立的头节点，那就加上一个。否则边界问题很难考虑

        i = head_head

        for _ in range(1, left):
            i = i.next

        stack = []
        j = i.next
        for _ in range(left, right + 1):
            if j is None:
                break
            stack.append(j)
            j = j.next

        while len(stack) > 0:
            node = stack.pop()
            i.next = node
            i = i.next
        i.next = j

        return head_head.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
l = s.reverseBetween(node1, 2, 4)

print(l)
