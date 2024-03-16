# https://leetcode.cn/problems/word-ladder/
from typing import List, Dict


class GraphNode:
    def __init__(self, val: str):
        self.val = val
        self.neighbors: List['GraphNode'] = []

    def add_neighbor(self, neighbor_node: 'GraphNode'):
        self.neighbors.append(neighbor_node)


class Solution:
    def __init__(self):
        self.graph: Dict[str, GraphNode] = {}

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(wordList)
        for i in range(n):
            for j in range(i + 1, n):
                if self.__is_neighbor_word__(wordList[i], wordList[j]):
                    self.__build_relation__(wordList[i], wordList[j])

        minimum_steps = 2 ** 32 - 1
        for i in range(n):
            if self.__is_neighbor_word__(beginWord, wordList[i]):
                steps = self.__dfs__(wordList[i], endWord, [])
                if 0 < steps < minimum_steps:
                    minimum_steps = steps

        if minimum_steps == 2 ** 32 - 1:
            return 0
        return minimum_steps + 1

    def __dfs__(self, begin_word: str, end_word: str, trace_stack: List[str]) -> int:
        if begin_word == end_word:
            return 1

        trace_stack.append(begin_word)

        minimum_steps = 2 ** 32 - 1
        begin_node = self.__get_or_create_node__(begin_word)

        for neighbor_node in begin_node.neighbors:
            if neighbor_node.val in trace_stack:
                continue

            steps = self.__dfs__(neighbor_node.val, end_word, trace_stack)
            if 0 < steps < minimum_steps:
                minimum_steps = steps

        trace_stack.pop()

        if minimum_steps == 2 ** 32 - 1:
            return -1

        return minimum_steps + 1

    def __build_relation__(self, val1: str, val2: str):
        node1 = self.__get_or_create_node__(val1)
        node2 = self.__get_or_create_node__(val2)
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)

    def __get_or_create_node__(self, val: str):
        if val not in self.graph:
            self.graph[val] = GraphNode(val)
        return self.graph[val]

    def __is_neighbor_word__(self, word1: str, word2: str):
        n = len(word1)
        diff_cnt = 0
        for i in range(n):
            if word1[i] != word2[i]:
                diff_cnt += 1

        return diff_cnt == 1


s = Solution()
print(s.ladderLength("qa", "sq", ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
