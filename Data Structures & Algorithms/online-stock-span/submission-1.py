class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        tempStack = self.stack.copy()
        self.stack.append(price)
        cnt = 1
        while tempStack and price >= tempStack[-1]:
            cnt += 1
            tempStack.pop()
        return cnt

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)