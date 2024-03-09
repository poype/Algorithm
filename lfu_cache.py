# https://leetcode.cn/problems/lfu-cache/description/


# 算法思路
# 用两个双向链表，一个链表就是用来存储key value的值。
# 另一个链表CountLinkNode，每个元素cnt是指访问的次数。所有key的访问次数是cnt值的LinkNode节点都会挂载到对应的CountLinkNode节点上。
class CountLinkNode(object):
    def __init__(self, cnt=1, pre=None, next=None):
        self.cnt = cnt
        self.num = 0
        self.val_head = LinkNode(-1, -1)
        self.pre = pre
        self.next = next


class LinkNode(object):
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
        self.num = 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.access_cnt_link = CountLinkNode(-1)
        self.access_cnt_link.next = self.access_cnt_link
        self.access_cnt_link.pre = self.access_cnt_link

        self.val_link = LinkNode()
        self.cnt_map = {}
        self.val_map = {}
        self.total_cnt = 0

    def get(self, key: int) -> int:
        if key not in self.val_map:
            return -1

        val_node = self.val_map[key]
        val_node.num += 1
        cnt_node = self.__get_or_create_cnt_node__(val_node.num)

        self.__move_val_node__(cnt_node, self.cnt_map[val_node.num - 1], val_node)

        return val_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.val_map:
            val_node = self.val_map[key]
            val_node.val = value
            val_node.num += 1
            cnt_node = self.__get_or_create_cnt_node__(val_node.num)

            self.__move_val_node__(cnt_node, self.cnt_map[val_node.num - 1], val_node)
        else:
            if self.total_cnt == self.capacity:
                self.__remove_last_node__()
                self.total_cnt -= 1

            if self.total_cnt == 0:
                cnt_node = CountLinkNode(1, self.access_cnt_link, self.access_cnt_link)
                self.access_cnt_link.next = cnt_node
                self.access_cnt_link.pre = cnt_node
                self.cnt_map[1] = cnt_node

            cnt_node = self.__get_or_create_cnt_node__(1)
            val_node = LinkNode(key, value)

            self.__add_val_node_to_cnt_link__(cnt_node, val_node)
            self.val_map[key] = val_node
            self.total_cnt += 1

    def __move_val_node__(self, new_cnt_node: CountLinkNode, old_cnt_node: CountLinkNode, val_node: LinkNode):
        val_node.pre.next = val_node.next
        val_node.next.pre = val_node.pre
        self.__add_val_node_to_cnt_link__(new_cnt_node, val_node)

        old_cnt_node.num -= 1

        if old_cnt_node.num == 0:
            old_cnt_node.pre.next = old_cnt_node.next
            old_cnt_node.next.pre = old_cnt_node.pre
            del self.cnt_map[old_cnt_node.cnt]

    def __add_val_node_to_cnt_link__(self, cnt_node: CountLinkNode, val_node: LinkNode):
        val_head = cnt_node.val_head

        if cnt_node.num == 0:
            val_head.next = val_node
            val_head.pre = val_node

            val_node.next = val_head
            val_node.pre = val_head
        else:
            val_node.next = val_head.next
            val_node.pre = val_head
            val_head.next.pre = val_node
            val_head.next = val_node

        cnt_node.num += 1

    def __get_or_create_cnt_node__(self, access_num: int) -> CountLinkNode:
        if access_num not in self.cnt_map:
            if access_num == 1:
                cnt_node = CountLinkNode(1)
                cnt_node.next = self.access_cnt_link
                cnt_node.pre = self.access_cnt_link.pre
                self.access_cnt_link.pre.next = cnt_node
                self.access_cnt_link.pre = cnt_node
            else:
                cnt_node = CountLinkNode(access_num)
                next_cnt_node = self.cnt_map[access_num - 1]
                cnt_node.next = next_cnt_node
                cnt_node.pre = next_cnt_node.pre
                next_cnt_node.pre.next = cnt_node
                next_cnt_node.pre = cnt_node

            self.cnt_map[access_num] = cnt_node

        return self.cnt_map[access_num]

    def __remove_last_node__(self):
        last_cnt_node = self.access_cnt_link.pre
        val_head = last_cnt_node.val_head
        last_val_node = val_head.pre
        last_val_node.pre.next = val_head
        val_head.pre = last_val_node.pre

        del self.val_map[last_val_node.key]

        last_cnt_node.num -= 1
        if last_cnt_node.num == 0:
            del self.cnt_map[last_cnt_node.cnt]
            last_cnt_node.pre.next = self.access_cnt_link
            self.access_cnt_link.pre = last_cnt_node.pre


cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
