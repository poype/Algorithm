class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.ordered_list) > 0:
            top_val = self.ordered_list[len(self.ordered_list) - 1]
            self.ordered_list.append(min(top_val, val))
        else:
            self.ordered_list.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
            self.ordered_list.pop()

    def top(self) -> int:
        top_idx = len(self.stack) - 1
        return self.stack[top_idx]

    def getMin(self) -> int:
        return self.ordered_list[len(self.ordered_list) - 1]
