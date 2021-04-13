class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.stack:
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if len(self.stack) == self.capacity:
                del self.cache[self.stack[0]]
                self.stack = self.stack[1:]
            self.cache[key] = value
            self.stack.append(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)