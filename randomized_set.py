# https://leetcode.cn/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150

import random


class RandomizedSet:
    def __init__(self):
        # key是数字val，value是数字在数组中的下标
        self.num_map_index = {}
        self.num_list = [0 for _ in range(2 * 100000)]
        self.size = 0

    def insert(self, val: int) -> bool:
        if val in self.num_map_index:
            return False

        self.num_list[self.size] = val
        self.num_map_index[val] = self.size
        self.size += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_map_index:
            return False

        index = self.num_map_index[val]
        last_num = self.num_list[self.size - 1]
        self.num_list[index] = last_num
        self.num_map_index[last_num] = index
        del self.num_map_index[val]
        self.size -= 1
        return True

    def getRandom(self) -> int:
        index = random.randint(0, self.size - 1)
        return self.num_list[index]


rs = RandomizedSet()
print(rs.insert(1))
print(rs.remove(2))
print(rs.insert(2))
print(rs.getRandom())
print(rs.remove(1))
print(rs.insert(2))
print(rs.getRandom())
