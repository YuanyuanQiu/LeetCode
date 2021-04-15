# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        a: before circle; b: circle
        1. f = 2s = s + nb -> f = 2nb, s = nb
        2. find entrance node: k = a + nb, now s in nb, need to get new from head
        and walk with s
        new = a -> s = a + nb -> slow in k and new in k
        '''
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        new = head
        while new != slow:
            new, slow = new.next, slow.next
        return new