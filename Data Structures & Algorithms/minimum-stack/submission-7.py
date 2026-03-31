class MinStack:

    def __init__(self):
        self.regStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.regStack.append(val)
        # prevMin = self.minStack[-1]
        val = min(val, self.minStack[-1] if self.minStack else 9999999999999)
        self.minStack.append(val)

    def pop(self) -> None:
        self.regStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.regStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
