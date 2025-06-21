class LinkNode:
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = LinkNode(None, None)
        self.tail = LinkNode(None, None, prev=self.head)
        self.head.nxt = self.tail
        self.capacity = capacity
        self.hash_table = defaultdict(LinkNode)
    
    def update(self, node):
        prev_node, nxt_node = node.prev, node.nxt
        prev_node.nxt = nxt_node
        nxt_node.prev = prev_node

        tail_prev = self.tail.prev

        tail_prev.nxt = node
        node.prev = tail_prev

        self.tail.prev = node
        node.nxt = self.tail

    def get(self, key: int) -> int:
        if key in self.hash_table:
            node = self.hash_table[key]
            self.update(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_table:
            node = self.hash_table[key]
            node.val = value
            self.update(node)
        else:
            if self.capacity == len(self.hash_table):
                rm_node = self.head.nxt
                self.head.nxt = rm_node.nxt
                rm_node.nxt.prev = self.head
                self.hash_table.pop(rm_node.key)

            tail_prev = self.tail.prev
            node = LinkNode(key, value, self.tail, tail_prev)
            tail_prev.nxt = node
            self.tail.prev = node
            self.hash_table[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)