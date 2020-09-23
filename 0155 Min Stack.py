# class MinStack:

#     def __init__(self):
#         self.ls = []

#     def push(self, x: int) -> None:
#         self.ls.append(x)

#     def pop(self) -> None:
#         self.ls.pop()

#     def top(self) -> int:
#         return self.ls[-1]

#     def getMin(self) -> int:
#         return min(self.ls)


# retrieving the minimum element in constant time.
class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1][0]
        
    def getMin(self):
        return self.stack[-1][1]