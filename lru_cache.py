from typing import Optional


class LinkNode(object):
    def __init__(self, key: int, val: int, pre: Optional['LinkNode'], next: Optional['LinkNode']):
        self.key = key
        self.val = val
        self.next = next
        self.pre = pre


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkNode(0, 0, None, None)
        self.map = {}
        self.cnt = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]

        self.__move_node_to_first__(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cnt == 0:
            node = LinkNode(key, value, self.head, self.head)
            self.map[key] = node
            self.head.next = node
            self.head.pre = node
            self.cnt += 1
        elif key in self.map:
            node = self.map[key]
            node.val = value

            self.__move_node_to_first__(node)
        else:
            node = LinkNode(key, value, self.head, self.head.next)
            self.head.next.pre = node
            self.head.next = node
            self.map[key] = node

            if self.cnt == self.capacity:
                last_node = self.head.pre
                last_node.pre.next = last_node.next
                last_node.next.pre = last_node.pre
                del self.map[last_node.key]
            else:
                self.cnt += 1

    def __move_node_to_first__(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.next = self.head.next
        node.pre = self.head

        self.head.next.pre = node
        self.head.next = node


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))