class MyHashMap:

    def __init__(self):
        self.capacity = 1009
        self.buckets = [[] for i in range(self.capacity)]
        
    def hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        for k, v in bucket:
            if k == key:
                bucket.remove([k, v])


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)