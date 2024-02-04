# https://leetcode.cn/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class GraphNode:
    def __init__(self, val: str):
        self.val = val
        self.neighbors = []

    def add_neighbor(self, neighbor_val: str):
        self.neighbors.append(neighbor_val)


class Solution:
    def __init__(self):
        self.result = -1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = {}
        bank.append(startGene)
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                if self.diff_cnt(bank[i], bank[j]) == 1:
                    if bank[i] not in graph:
                        graph[bank[i]] = GraphNode(bank[i])
                    if bank[j] not in graph:
                        graph[bank[j]] = GraphNode(bank[j])
                    graph[bank[i]].add_neighbor(bank[j])
                    graph[bank[j]].add_neighbor(bank[i])

        if endGene not in graph:
            return -1

        self.dfs(graph, startGene, endGene, [], 0)

        return self.result

    def dfs(self, graph: dict[str, GraphNode], startGene: str, endGene: str, stack: List[str], steps: int):
        if startGene == endGene:
            if self.result == -1:
                self.result = steps
            elif self.result > steps:
                self.result = steps
            return

        stack.append(startGene)
        start_node = graph[startGene]

        for neighbor_val in start_node.neighbors:
            if neighbor_val not in stack:
                self.dfs(graph, neighbor_val, endGene, stack, steps + 1)

        stack.pop()

    def diff_cnt(self, str1: str, str2: str):
        cnt = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                cnt += 1

        return cnt


s = Solution()
start = "AAAAAAAA"
end = "AAAAACGG"
bank = ["AAAAAAGA","AAAAAGGA","AAAAACGA","AAAAACGG","AAAAAAGG","AAAAAAGC"]

print(s.minMutation(start, end, bank))
