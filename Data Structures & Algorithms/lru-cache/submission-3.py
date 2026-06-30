#Make Node Class. They will hold the key and val ints. Also give prev and next pts to none
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        #Initialize params and right/leftpointers and their next/prev
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
        
    #Creade New node and make MRU adjust pointers using righ and left as basis
    def insert_node(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev
    
    #Delete Node and adjust pointers
    def delete_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    #Check cache, delete node, create node, return key/val if not return -1
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete_node(self.cache[key])
            self.insert_node(self.cache[key])
            return self.cache[key].val
        return -1


    #If key already in, delete from Cache. Outside, put in cache and make node 
    #If cache too big, get the LRU, delete the node and HM
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_node(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.delete_node(lru)
            del self.cache[lru.key]
        
