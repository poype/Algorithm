# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):   # 当自己引用自己的类型，可以给类型加上单引号
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Optional[Node]:
        queue = []
        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            next_queue = []

            while len(queue) > 0:
                tree_node = queue.pop(0)
                if len(queue) > 0:
                    tree_node.next = queue[0]

                if tree_node.left is not None:
                    next_queue.append(tree_node.left)

                if tree_node.right is not None:
                    next_queue.append(tree_node.right)

            queue = next_queue

        return root


root = Node(0)
s = Solution()
s.connect(root)
