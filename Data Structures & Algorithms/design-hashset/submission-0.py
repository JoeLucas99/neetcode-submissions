class MyHashSet:

    def __init__(self):
        self.mySet = []
        

    def add(self, key: int) -> None:
        self.key = key
        for num in self.mySet:
            if num == self.key:
                return
        self.mySet.append(self.key)
        

    def remove(self, key: int) -> None:
        self.key = key
        for num in self.mySet:
            if num == self.key:
                self.mySet.remove(self.key)

    def contains(self, key: int) -> bool:
        self.key = key
        for num in self.mySet:
            if num == self.key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)