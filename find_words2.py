# https://leetcode.cn/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        result = []
        for word in words:
            if self.__is_word_in_board__(board, word):
                result.append(word)
        return result

    def __is_word_in_board__(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.__dfs__(board, word, 0, i, j, []):
                    return True

        return False

    def __dfs__(self, board: List[List[str]], word: str, idx: int, row: int, column: int, trace_stack: List) -> bool:
        trace_stack.append(f"{row}_{column}")

        if board[row][column] != word[idx]:
            trace_stack.pop()
            return False

        if idx == len(word) - 1:
            return True

        if (column < (len(board[0]) - 1) and
                f"{row}_{column + 1}" not in trace_stack and
                self.__dfs__(board, word, idx + 1, row, column + 1, trace_stack)):
            return True

        if (row < len(board) - 1 and
                f"{row + 1}_{column}" not in trace_stack and
                self.__dfs__(board, word, idx + 1, row + 1, column, trace_stack)):
            return True

        if (column > 0 and
                f"{row}_{column - 1}" not in trace_stack and
                self.__dfs__(board, word, idx + 1, row, column - 1, trace_stack)):
            return True

        if (row > 0 and
                f"{row - 1}_{column}" not in trace_stack and
                self.__dfs__(board, word, idx + 1, row - 1, column, trace_stack)):
            return True

        trace_stack.pop()
        return False


board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ["abcdefg"]

s = Solution()
print(s.findWords(board, words))
