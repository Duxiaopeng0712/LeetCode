from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        i = 0
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop())

    def top(self) -> int:
        while self.queue1 > 1:
            self.queue2.append(self.queue1.pop())
        temp = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return temp

    def empty(self) -> bool:
        return not bool(self.queue1)
