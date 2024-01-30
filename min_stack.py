class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.ordered_list.append(val)
        self.ordered_list.sort()

    def pop(self) -> None:
        if len(self.stack) > 0:
            top_val = self.top()
            self.stack.pop()
            self.ordered_list.remove(top_val)
            self.ordered_list.sort()

    def top(self) -> int:
        top_idx = len(self.stack) - 1
        return self.stack[top_idx]

    def getMin(self) -> int:
        return self.ordered_list[0]
