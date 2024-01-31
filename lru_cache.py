class LinkNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 为了能让put和get在 O(1)内完成，使用dick
        self.stack_head = LinkNode()
        self.stack_head.next = self.stack_head
        self.stack_head.prev = self.stack_head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        p = self.cache[key]

        p.prev.next = p.next
        if p.next is not None:
            p.next.prev = p.prev

        if self.stack_head.prev == p:
            self.stack_head.prev = p.prev

        p.next = self.stack_head.next
        p.prev = self.stack_head

        self.stack_head.next.prev = p
        self.stack_head.next = p
        return p.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:   # update
            p = self.cache[key]
            p.val = value
            self.get(key)
            return

        # add
        p = LinkNode(key, value, self.stack_head.next, self.stack_head)
        self.stack_head.next.prev = p
        self.stack_head.next = p

        self.cache[key] = p

        if len(self.cache) > self.capacity:
            last = self.stack_head.prev
            self.stack_head.prev = last.prev
            last.prev.next = self.stack_head

            del self.cache[last.key]


cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))
print(cache.get(2))
