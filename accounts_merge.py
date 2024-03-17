# https://leetcode.cn/problems/accounts-merge/

from typing import List, Dict


class UnionFind(object):
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, idx: int):
        if self.parent[idx] == idx:
            return idx

        return self.find(self.parent[idx])

    def union(self, idx1: int, idx2: int):
        # self.parent[idx2] = self.parent[idx1] 这行代码不行，可能造成一个集合分裂
        self.parent[self.find(idx2)] = self.find(idx1)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_dict = self.__create_email_dict__(accounts)

        uf = UnionFind(len(accounts))
        self.__build_uf__(email_dict, uf)

        # key是每个组带头大哥的下标，value是包含组中所有member下标的list
        group_dict = self.__create_group_dict__(uf, len(accounts))

        result = []
        for group_id_key in group_dict.keys():
            username = accounts[group_id_key][0]

            new_account = []
            for member_idx in group_dict[group_id_key]:
                account = accounts[member_idx]
                for i in range(1, len(account)):
                    email = account[i]
                    if email not in new_account:
                        new_account.append(email)

            new_account.sort()
            new_account.insert(0, username)
            result.append(new_account)
        return result

    def __create_group_dict__(self, uf: UnionFind, cnt: int) -> Dict[int, List[int]]:
        group_dict: Dict[int, List[int]] = {}
        for i in range(cnt):
            parent = uf.find(i)
            if parent not in group_dict:
                group_dict[parent] = []
            group_dict[parent].append(i)

        return group_dict

    def __build_uf__(self, email_dict: Dict[str, List[int]], uf: UnionFind):
        for idx_list in email_dict.values():
            parent = idx_list[0]
            for i in range(1, len(idx_list)):
                uf.union(parent, idx_list[i])

    def __create_email_dict__(self, accounts: List[List[str]]) -> Dict[str, List[int]]:
        """
        :return: key是email，value是包含email的account的数组下标
        """
        email_dict: Dict[str, List[int]] = {}

        for i in range(len(accounts)):
            account = accounts[i]
            for j in range(1, len(account)):
                email = account[j]
                if email not in email_dict:
                    email_dict[email] = []
                email_dict[email].append(i)

        return email_dict


s = Solution()
accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"]]

print(s.accountsMerge(accounts))
