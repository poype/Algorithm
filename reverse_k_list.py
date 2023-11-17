from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 算法思想是用两个指针p,q定位好一个段的起始地址和结束地址，然后用头插法逆转
class Solution(object):
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head

        temp_head = ListNode()
        h = temp_head

        while p is not None:
            q = p
            # q指针往后走 k-1 步，指向一段的结束位置
            q = self.move_k_steps(q, k - 1)
            if q is None:
                break

            # 记录下一段的开始地址
            next_start = q.next

            # 头插法逆转
            o = p
            for i in range(k):
                r = o.next
                o.next = h.next
                h.next = o
                o = r

            # 原来p指针指向一段的第一个节点，经过逆转之后，p指针指向了该段的最后一个节点
            # h指向逆转后本段的最后一个节点，作为下一段的头节点
            h = p

            p = next_start

        # 可能还剩余几个节点无需逆转，要跟在链表的最后
        h.next = p

        return temp_head.next

    def move_k_steps(self, p: ListNode, k: int) -> ListNode | None:
        """
        让一个指针向前走k步
        :param p: 指针
        :param k: 步数
        :return: 如果剩余的节点足够让指针走k步，返回走k步后对应的指针。如果剩余的节点不足，返回None
        """
        if p is None:
            return p

        while k > 0:
            p = p.next
            if p is None:
                return None
            k -= 1

        return p


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(3)
l2.next = l3
l4 = ListNode(4)
l3.next = l4
l5 = ListNode(5)
l4.next = l5
l6 = ListNode(6)
l5.next = l6
l7 = ListNode(7)
l6.next = l7
l8 = ListNode(8)
l7.next = l8
l9 = ListNode(9)
l8.next = l9

s = Solution()
result = s.reverseKGroup(l1, 4)

print(result)
