# Initialize adouble linked list for this problem
#The cache is fully connected.
# a dictionnary is here to record the codependy of the nodes

# The trick is to consider the action of "getting" as a removal and an insertion

# We have 2 gards : left and right, initialize as nodes that delimitate the boundaries of the linked list

# To remove an element, we just take a look at the linked list,see the next element of the left pointerand remove the node
# To add an element, we look at the previous element at the right pointer and add the node.


## This is a critical exercise to remember !!!
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        self.size = 0

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.size -= 1
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        self.size +=1

        if self.size > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            self.cache.pop(lru.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)