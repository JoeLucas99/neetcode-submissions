class MyHashMap:

    def __init__(self):
        self.capacity = 1009
        self.hash_set = [[] for i in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return
        self.hash_set[ind].append([key, value])

    def get(self, key: int) -> int:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        ind = self.hash(key)
        bucket = self.hash_set[ind]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                self.hash_set[ind].remove(bucket[i])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)