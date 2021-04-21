class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.stack = []

    def get(self, key: int) -> int:
        if key in self.dic:
            self.stack.remove(key)
            self.stack.append(key)
            return self.dic[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.stack.remove(key)
            self.dic[key] = value
        else:
            if len(self.stack) == self.capacity:
                del self.dic[self.stack[0]]
                del self.stack[0]
            self.dic[key] = value
        self.stack.append(key)