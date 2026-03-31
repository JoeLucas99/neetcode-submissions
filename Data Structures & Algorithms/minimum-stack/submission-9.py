class MinStack:

    def __init__(self):
        self.minStack = []
        self.curMin = []
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        self.val = min(val, self.curMin[-1] if self.curMin else float("inf"))
        self.curMin.append(self.val)


    def pop(self) -> None:
        self.minStack.pop()
        self.curMin.pop()

    def top(self) -> int:
        return self.minStack[-1]

    def getMin(self) -> int:
        return self.curMin[-1]
