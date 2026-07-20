class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove the node
            self.remove(self.cache[key])
            # then insert the key to the end
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


cache = LRUCache(3)
# LRUCache lRUCache = new LRUCache(2);
cache.get(1) # return -1
cache.put(2, 5) # cache: {2:5}
cache.get(2) # return 5
cache.put(1, 4) # cache: {2:5, 1:4}
cache.put(3, 4) # cache: {2:5, 1:4, 3:4}
cache.put(5, 2) # cache: {1:4, 3:4, 5:2}, key=1 was evicted
cache.get(5) # return 2
print(cache.get(2)) # return -1



        
