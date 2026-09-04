#"Hash" the numbers using mod
#Then do bucket sort
class MyHashSet:
    def __init__(self):
        self.capacity = 1009
        self.buckets = [[] for i in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        indx = self.hash(key)
        bucket = self.buckets[indx]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)