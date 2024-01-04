# https://leetcode.cn/problems/excel-sheet-column-title/description/

# 几个英文单词
# division 除法   9 / 3 = 3
# 被除数 dividend  9
# 除数 divisor  3
# 商 quotient
# 余数 remainder

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_char_map = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
        }

        remainder = columnNumber % 26
        quotient = columnNumber // 26
        result = ""

        while quotient > 0:
            if remainder == 0:
                remainder = 26
                quotient = quotient - 1  # 进位少1

            result = f"{num_char_map[remainder]}{result}"

            remainder = quotient % 26
            quotient = quotient // 26

        if remainder > 0:
            result = f"{num_char_map[remainder]}{result}"

        return result


s = Solution()
print(s.convertToTitle(52))