# https://leetcode.cn/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        self.handle_remain_path(result, path)

        if len(result) == 0:
            return "/"
        else:
            return "".join(result)

    def handle_remain_path(self, result: List[str], remain_path: str):
        i = 1
        while i < len(remain_path) and remain_path[i] == '/':
            i += 1

        if i < len(remain_path):
            idx = remain_path.find('/', i)
            if idx == -1:
                self.append_relative_path(result, remain_path[i - 1:])
            else:
                self.append_relative_path(result, remain_path[i - 1: idx])
                self.handle_remain_path(result, remain_path[idx:])

    def append_relative_path(self, result: List[str], relative_path: str):
        if len(relative_path) == 3 and relative_path[1] == "." and relative_path[2] == ".":
            if len(result) > 0:
                result.pop()
        elif len(relative_path) != 2 or relative_path[1] != ".":
            result.append(relative_path)


s = Solution()
path = "/a/./b/../../c/"

print(s.simplifyPath(path))
