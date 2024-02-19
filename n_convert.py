# https://leetcode.cn/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, num_rows):
        if num_rows == 1:
            return s

        # 一个周期包含 num_rows + num_rows - 2 个字符
        circle_char_number = num_rows + num_rows - 2
        circle_length = num_rows - 1
        max_column_number = (len(s) // circle_char_number + 1) * circle_length

        matrix = [['' for _ in range(max_column_number)] for _ in range(num_rows)]
        p, i, j = 0, 0, 0
        while p < len(s):
            while i < num_rows and p < len(s):
                matrix[i][j] = s[p]
                p += 1
                i += 1

            j += 1
            i -= 2
            while i >= 1 and p < len(s):
                matrix[i][j] = s[p]
                p += 1
                i -= 1
                j += 1

        result = ""
        for row in range(num_rows):
            for column in range(max_column_number):
                if matrix[row][column] != '':
                    result += matrix[row][column]

        return result


s = Solution()
print(s.convert("A", 1))
