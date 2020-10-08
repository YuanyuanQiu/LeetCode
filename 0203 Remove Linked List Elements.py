# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        pre, cur = sentinel, head
        while cur:
            if cur == val:
                pre.next = cur.next
            else:
                pre.cur = cur
            cur = cur.next
        
        # 如果head.val是val的话，sentinel.next就不是head了
        return sentinel.next