# https://leetcode.cn/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150


class TreeNode:
    def __init__(self, val: str):
        self.val = val
        self.children = {}

    def __add_child__(self, child: 'TreeNode'):
        self.children[child.val] = child


class Trie:

    def __init__(self):
        self.root = TreeNode("root")
        self.node_dict = {}
        self.word_set = set()

    def insert(self, word: str) -> None:
        self.word_set.add(word)

        node = self.__create_node__(word[0], 0)
        self.root.__add_child__(node)

        parent_node = node
        for i in range(1, len(word)):
            node = self.__create_node__(word[i], i)
            parent_node.__add_child__(node)
            parent_node = node

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.children:
                return False
            node = node.children[prefix[i]]

        return True

    def __create_node__(self, val: str, level: int):
        key = f"{level}{val}"
        if key not in self.node_dict:
            self.node_dict[key] = TreeNode(val)
        return self.node_dict[key]


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))     # 返回 True
print(trie.search("app"))       # 返回 False
print(trie.startsWith("app"))   # 返回 True
trie.insert("app")
print(trie.search("app"))
