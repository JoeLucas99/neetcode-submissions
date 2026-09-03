class MyHashSet:

    def __init__(self):
        self.capacity = 1009
        self.hash_set = [[] for i in range(self.capacity)]
        
    def hash(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        if key not in bucket:
            self.hash_set[ind].append(key)

    def remove(self, key: int) -> None:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        if key in bucket:
            self.hash_set[ind].remove(key)

    def contains(self, key: int) -> bool:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        return key in bucket

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)