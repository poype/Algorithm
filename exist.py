# https://leetcode.cn/problems/word-search/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.__dfs__(board, i, j, word, 0, []):
                    return True

        return False

    def __dfs__(self, board: List[List[str]], row: int, column: int, word: str, idx: int,
                trace_stack: List[str]) -> bool:

        if idx == len(word) - 1:
            if board[row][column] != word[idx]:
                return False
            return True

        trace_stack.append(f"{row}_{column}")

        if board[row][column] != word[idx]:
            trace_stack.pop()
            return False

        if (column < len(board[0]) - 1 and
                f"{row}_{column + 1}" not in trace_stack and
                self.__dfs__(board, row, column + 1, word, idx + 1, trace_stack)):
            return True

        if (row < len(board) - 1 and
                f"{row + 1}_{column}" not in trace_stack and
                self.__dfs__(board, row + 1, column, word, idx + 1, trace_stack)):
            return True

        if (column > 0 and
                f"{row}_{column - 1}" not in trace_stack and
                self.__dfs__(board, row, column - 1, word, idx + 1, trace_stack)):
            return True

        if (row > 0 and
                f"{row - 1}_{column}" not in trace_stack and
                self.__dfs__(board, row - 1, column, word, idx + 1, trace_stack)):
            return True

        trace_stack.pop()
        return False


s = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"

print(s.exist(board, word))
