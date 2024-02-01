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
        if root is None:
            return root

        level = []
        self.add_child_to_list(level, root)

        while len(level) > 0:
            next_level = []
            for i in range(len(level) - 1):
                self.add_child_to_list(next_level, level[i])
                level[i].next = level[i + 1]

            self.add_child_to_list(next_level, level[len(level) - 1])

            level = next_level

        return root

    def add_child_to_list(self, level: List[Node], node: Node):
        if node.left is not None:
            level.append(node.left)

        if node.right is not None:
            level.append(node.right)


root = Node(0)
s = Solution()
s.connect(root)
