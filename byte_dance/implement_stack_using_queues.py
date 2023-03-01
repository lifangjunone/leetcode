class MyStack:

    def __init__(self):
        self.inqueue = []
        self.outqueue = []

    def push(self, x: int) -> None:
        self.inqueue.insert(0, x)

    def pop(self) -> int:
        while self.inqueue:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue.pop()

    def top(self) -> int:
        while self.inqueue:
            self.outqueue.append(self.inqueue.pop())
        return self.outqueue[-1]

    def empty(self) -> bool:
        return not len(self.inqueue) and not len(self.outqueue)
