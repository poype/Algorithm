# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.path_stack = []
        self.p_path = []
        self.q_path = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.__traverse__(root, p, q)

        if len(self.q_path) > len(self.p_path):
            self.p_path, self.q_path = self.q_path, self.p_path

        p_idx = len(self.p_path) - 1
        q_idx = len(self.q_path) - 1

        while p_idx > q_idx:
            p_idx -= 1

        while self.p_path[p_idx] != self.q_path[q_idx]:
            p_idx -= 1
            q_idx -= 1

        return self.p_path[p_idx]

    def __traverse__(self, root: TreeNode, p: TreeNode, q: TreeNode):
        if len(self.p_path) > 0 and len(self.q_path) > 0:
            return

        self.path_stack.append(root)

        if root == p:
            self.p_path = self.path_stack[:]
        elif root == q:
            self.q_path = self.path_stack[:]

        if root.left is not None:
            self.__traverse__(root.left, p, q)

        if root.right is not None:
            self.__traverse__(root.right, p, q)

        self.path_stack.pop()


node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

s = Solution()
result = s.lowestCommonAncestor(node3, node5, node4)
print(result)
