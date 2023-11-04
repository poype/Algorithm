# https://leetcode.cn/problems/longest-palindromic-substring/

class Solution(object):

    def __init__(self):
        # 定义一个类成员变量
        self.matrix = None

    def longestPalindrome(self, s):
        """
        :type s: str
        """
        max_length = 0
        result = ""
        # init matrix
        self.matrix = [[None for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s) - 1, -1, -1):
                if self.is_palindrome(s, i, j) and j - i + 1 > max_length:
                    max_length = j - i + 1
                    result = s[i: j + 1]

        return result

    def is_palindrome(self, s, start, end):
        """
        判断字符串s中的子序列是否是回文字符串
        :param s: 目标字符串
        :param start: 起始索引
        :param end: 终止索引
        :return: 回文字符串返回True，否则返回False
        """
        if self.matrix[start][end] is not None:
            return self.matrix[start][end]

        if start == end:
            self.matrix[start][end] = True
            return True
        elif start > end:
            self.matrix[start][end] = False
            return False

        if s[start] != s[end]:
            self.matrix[start][end] = False
            return False
        elif end - start == 1:
            self.matrix[start][end] = True
            return True
        else:
            check_result = self.is_palindrome(s, start + 1, end - 1)
            self.matrix[start][end] = check_result
            return check_result


s = Solution()
print(s.longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))
