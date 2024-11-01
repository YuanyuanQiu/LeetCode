class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0

        # store key-node pair
        self.cache = {}

        # 双向链表
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # 节点不存在
        if key not in self.cache:
            return -1
        # 节点存在
        node = self.cache[key] # 取值
        self.move_to_head(node) # 从原来位置删除并插入到头部
        return node.val

    def put(self, key: int, value: int) -> None:
        # 节点存在
        if key in self.cache:
            node = self.cache[key] # 取值
            node.val = value # 更新value
            self.move_to_head(node) # 从链表原来位置删除并插入到链表头部
        # 节点不存在
        else:
            node = Node(key, value) # 新建node
            self.cache[key] = node # 更新字典
            self.add_to_head(node) # 插入到链表头部
            self.size += 1 # 更新size
            # 如果size超过capacity
            if self.size > self.capacity:
                node = self.remove_tail() # 从链表尾部删除
                self.cache.pop(node.key) # 从字典删除
                self.size -= 1 # 更新size

    # 从链表原来位置删除并插入到链表头部
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    # 从链表原来位置删除
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 插入到链表头部
    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    # 删除链表尾部的节点
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)