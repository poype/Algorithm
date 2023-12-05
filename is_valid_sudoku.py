from typing import List


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.has_duplicate_number([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]):
                return False

        for column in range(9):
            if self.has_duplicate_number([board[0][column], board[1][column], board[2][column], board[3][column],
                                          board[4][column], board[5][column], board[6][column], board[7][column],
                                          board[8][column]]):
                return False

        for m in range(3):
            for n in range(3):  # 一共9组
                items = []
                for i in range(3 * m, 3 * (m + 1)):  # row
                    for j in range(3 * n, 3 * (n + 1)):  # column
                        items.append(board[i][j])

                if self.has_duplicate_number(items):
                    return False
        return True

    def has_duplicate_number(self, items: List[str]):
        s = set()
        dot_num = 0
        for item in items:
            if item == '.':
                dot_num += 1
            else:
                s.add(item)

        return len(s) + dot_num < len(items)


s = Solution()
board = \
    [[".", ".", ".", ".", "5", ".", ".", "1", "."],
     [".", "4", ".", "3", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
     [".", ".", "2", ".", "7", ".", ".", ".", "."],
     [".", "1", "5", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "2", ".", ".", "."],
     [".", "2", ".", "9", ".", ".", ".", ".", "."],
     [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(s.isValidSudoku(board))
