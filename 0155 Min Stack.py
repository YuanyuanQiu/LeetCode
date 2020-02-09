# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:04:27 2020

@author: ToxicCat
"""
# stack=[]

# def push(x: int) -> None:
#     stack.append(x)
    

# def pop() -> None:
#     if stack != []:
#         stack.pop()

# def top() -> int:
#     if stack != []:
#         return stack[-1]

# def getMin() -> int:
#     if stack != []:
#         return min(stack)



self.data = []
# 辅助栈
self.helper = []

def push(self, x):
    self.data.append(x)
    if len(self.helper) == 0 or x <= self.helper[-1]: #确保helper不为空且存min
        self.helper.append(x)
    else:
        self.helper.append(self.helper[-1])

def pop(self):
    if self.data:
        self.helper.pop()
        return self.data.pop()

def top(self):
    if self.data:
        return self.data[-1]

def getMin(self):
    if self.helper:
        return self.helper[-1]
