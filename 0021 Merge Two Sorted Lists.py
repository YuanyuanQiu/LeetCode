# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l1 = ListNode(1)
l12 = ListNode(2)
l13 = ListNode(4)
l1.next = l12
l12.next = l13

l2 = ListNode(1)
l22 = ListNode(3)
l23 = ListNode(4)
l2.next = l22
l22.next = l23

def printBackward(ln):
    if ln == None:
        return
    printBackward(ln.next)
    print(ln.val)

printBackward(l1)


'''
我们可以如下递归地定义两个链表里的 merge 操作（忽略边界情况，比如空链表等）：
- list1[0] + merge(list1[1:], list2)  if list1[0] < list2[0]
- list2[0] + merge(list1, list2[1:])  if list1[0] > list2[0]
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        # 递归
        if l1.val <= l2.val:  
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
