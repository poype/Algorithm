# https://leetcode.cn/problems/group-anagrams/

from typing import List

# dict的用法，字符串排序

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for str in strs:
            key = self.sort_str(str)
            if not map.__contains__(key):
                map[key] = []
            map[key].append(str)

        result = []
        for key in map.keys():
            result.append(map[key])

        return result

    def sort_str(self, str):
        arr = []

        for ch in str:
            arr.append(ch)

        arr.sort()

        return "".join(arr)



s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))