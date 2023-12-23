# https://leetcode.cn/problems/word-ladder/
from typing import List, Set


class GraphNode:
    def __init__(self, val: str):
        self.val = val
        self.neighbors = set()

    def add_neighbor(self, another_node):
        self.neighbors.add(another_node)


class Solution:
    def __init__(self):
        self.word_node_dict = {}
        self.steps = 0
        self.max_steps = 99999999

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        all_word_list = []
        all_word_list.extend(wordList)
        all_word_list.append(beginWord)

        for word in all_word_list:
            self.create_or_get_graph_node(word)
            for another_word in all_word_list:
                if another_word == word:
                    continue
                if self.can_convert(word, another_word):
                    self.add_neighbor_for_both_word(word, another_word)

        begin_word_node = self.word_node_dict[beginWord]
        self.dfs(begin_word_node, endWord, set())

        if self.max_steps == 99999999:
            return 0
        return self.max_steps

    def dfs(self, current_node: GraphNode, end_word: str, trace: Set):
        self.steps += 1
        trace.add(current_node.val)
        if current_node.val == end_word:
            if self.steps < self.max_steps:
                self.max_steps = self.steps
            self.steps -= 1
            trace.remove(current_node.val)
            return

        for neighbor in current_node.neighbors:
            if trace.__contains__(neighbor.val):
                continue
            self.dfs(neighbor, end_word, trace)

        self.steps -= 1
        trace.remove(current_node.val)

    def create_or_get_graph_node(self, val: str) -> GraphNode:
        if not self.word_node_dict.__contains__(val):
            self.word_node_dict[val] = GraphNode(val)

        return self.word_node_dict[val]

    def can_convert(self, word1: str, word2: str) -> bool:
        diff_count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False

        return True

    def add_neighbor_for_both_word(self, word1: str, word2: str):
        word1_node = self.create_or_get_graph_node(word1)
        word2_node = self.create_or_get_graph_node(word2)
        word1_node.add_neighbor(word2_node)
        word2_node.add_neighbor(word1_node)


s = Solution()
print(s.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
