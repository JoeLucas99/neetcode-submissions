class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left_node = Node(0,0)
        self.right_node = Node(0,0)
        self.left_node.next = self.right_node
        self.right_node.prev = self.left_node
        
    def add_node(self, node):
        new_right = self.right_node
        new_left = self.right_node.prev
        node.next = new_right
        node.prev = new_left
        new_left.next = node
        new_right.prev = node

    def remove_node(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left_node.next
            self.remove_node(lru)
            del self.cache[lru.key]
        
