# https://leetcode.cn/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150

class TreeNode:
    def __init__(self, value: str):
        self.value = value
        self.children = {}
        self.last_ch_flag = False

    def add_child(self, child_node: 'TreeNode'):
        self.children[child_node.value] = child_node

    def set_last_ch(self):
        self.last_ch_flag = True


class WordDictionary:

    def __init__(self):
        self.root = TreeNode("root")
        self.tree = {}

    def addWord(self, word: str) -> None:
        parent_node = self.root
        for i in range(len(word)):
            key = f"{i}{word[i]}"
            if key not in self.tree:
                self.tree[key] = TreeNode(word[i])
            parent_node.add_child(self.tree[key])
            parent_node = self.tree[key]

            if i == len(word) - 1:
                self.tree[key].set_last_ch()

    def search(self, word: str) -> bool:
        return self.__dfs__(self.root, word, 0)

    def __dfs__(self, root: TreeNode, word: str, idx: int) -> bool:
        if idx == len(word) - 1:
            if word[idx] == '.':
                for child_node in root.children.values():
                    if child_node.last_ch_flag:
                        return True
                return False
            else:
                if word[idx] not in root.children:
                    return False
                if root.children[word[idx]].last_ch_flag:
                    return True
                return False

        if word[idx] == '.':
            for child_node in root.children.values():
                if self.__dfs__(child_node, word, idx + 1):
                    return True
        else:
            if word[idx] not in root.children:
                return False
            if self.__dfs__(root.children[word[idx]], word, idx + 1):
                return True

        return False


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))