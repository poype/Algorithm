# https://leetcode.cn/problems/add-two-numbers/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode()
        p = head
        carry = 0

        while l1 is not None and l2 is not None:
            val = (carry + l1.val + l2.val) % 10
            carry = (carry + l1.val + l2.val) // 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None:
            l1 = l2

        while l1 is not None:
            val = (carry + l1.val) % 10
            carry = (carry + l1.val) // 10
            p.next = ListNode(val)
            p = p.next
            l1 = l1.next

        if carry > 0:
            p.next = ListNode(carry)

        return head.next


l1 = ListNode(2)
l1b = ListNode(4)
l1.next = l1b
l1c = ListNode(3)
l1b.next = l1c

l2 = ListNode(5)
# l2b = ListNode(6)
# l2.next = l2b
# l2c = ListNode(4)
# l2b.next = l2c

s = Solution()
l3 = s.addTwoNumbers(l1, l2)

print("--")

