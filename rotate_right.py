# https://leetcode.cn/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head  # 这个链表没有头节点，不用想别的，先给它增加一个头节点

        p = head
        cnt = 0
        while p is not None:
            cnt += 1
            p = p.next

        if cnt == 0:
            return head

        k = k % cnt  # k 可能大于链表的长度

        i, j = head_head, head_head
        for _ in range(k):
            j = j.next

        while j is not None:
            j = j.next
            i = i.next

        k = head_head
        while k.next != i:
            k = k.next
        k.next = None

        stack = []
        while i is not None:
            stack.append(i)
            i = i.next

        while len(stack) > 0:
            node = stack.pop()
            node.next = head_head.next
            head_head.next = node

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

