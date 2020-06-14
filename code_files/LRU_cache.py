class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = dict()


    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self.delete(node)
        self.append(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.delete(self.table[key])
        self.append(Node(key, value))
        if len(self.table) > self.cap:
            self.delete(self.tail.prev)


    def append(self, node):
        self.table[node.key] = node
        n = self.head.next
        self.head.next = node
        node.next = n
        node.prev = self.head
        n.prev = node


    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

        # n = node.next
        # p = node.prev
        # n.prev = p
        # p.next = n
        del self.table[node.key]
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)