# https://leetcode.cn/problems/reverse-nodes-in-k-group/
from typing import Optional, List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head
        stack_list = []

        p = head_head
        start = head
        end = self.__move_k_step__(start, k)
        while end is not None:
            next_start = end.next
            stack_list.append(self.__split_group__(start, end))
            start = next_start
            end = self.__move_k_step__(start, k)

        for i in range(len(stack_list)):
            stack = stack_list[i]
            while len(stack) > 0:
                node = stack.pop()
                p.next = node
                p = p.next

        p.next = start

        return head_head.next

    def __split_group__(self, start: ListNode, end: ListNode) -> List[ListNode]:
        stack = []
        p = start
        while p != end:
            stack.append(p)
            p = p.next

        stack.append(end)
        return stack

    def __move_k_step__(self, start: ListNode, k: int) -> Optional[ListNode]:
        i, end = 1, start
        while i < k:
            if end is None:
                break

            end = end.next
            i += 1

        if i < k:
            return None

        return end


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5
# l6 = ListNode(6)
# l5.next = l6
# l7 = ListNode(7)
# l6.next = l7
# l8 = ListNode(8)
# l7.next = l8
# l9 = ListNode(9)
# l8.next = l9

s = Solution()
result = s.reverseKGroup(l1, 2)

print(result)
