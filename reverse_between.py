# https://leetcode.cn/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head_head = ListNode()
        head_head.next = head

        p_left_pre = self.__get_p_of_pos__(head_head, left - 1)
        p_left = self.__get_p_of_pos__(head_head, left)
        p_right = self.__get_p_of_pos__(head_head, right)
        p_right_next = p_right.next

        p = p_left.next
        while p != p_right_next:
            q = p.next
            p.next = p_left_pre.next
            p_left_pre.next = p
            p = q

        p_left.next = p_right_next
        return head_head.next

    def __get_p_of_pos__(self, head: ListNode, pos: int) -> ListNode:
        p = head
        for _ in range(pos):
            p = p.next
        return p


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
