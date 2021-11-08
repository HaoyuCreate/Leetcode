class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        num = temp.pop()
        while temp:
            self.stack.append(temp.pop())
        return num

    def peek(self) -> int:
        temp = []
        while self.stack:
            temp.append(self.stack.pop())
        num = temp[-1]
        while temp:
            self.stack.append(temp.pop())
        return num

    def empty(self) -> bool:
        return len(self.stack) == 0