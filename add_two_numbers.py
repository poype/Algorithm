# https://leetcode.cn/problems/add-two-numbers/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1, p2 = l1, l2
        head = ListNode()
        p = head
        carry = 0
        while p1 is not None and p2 is not None:
            p = self.add_new_node(p, (p1.val + p2.val + carry))
            carry = 1 if (p1.val + p2.val + carry) >= 10 else 0
            p1 = p1.next
            p2 = p2.next

        if p1 is None:
            p1 = p2

        while p1 is not None:
            p = self.add_new_node(p, p1.val + carry)
            carry = 1 if (p1.val + carry) >= 10 else 0
            p1 = p1.next

        if carry > 0:
            q = ListNode(carry)
            p.next = q

        return head.next

    def add_new_node(self, p: ListNode, sum_val: int) -> ListNode:
        q = ListNode(sum_val % 10)
        p.next = q
        p = p.next
        return p


l1 = ListNode(2)
l1b = ListNode(4)
l1.next = l1b
l1c = ListNode(3)
l1b.next = l1c

l2 = ListNode(5)
l2b = ListNode(6)
l2.next = l2b
l2c = ListNode(4)
l2b.next = l2c

s = Solution()
l3 = s.addTwoNumbers(l1, l2)

print("--")

