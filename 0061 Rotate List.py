def rotateRight(self, head: ListNode, k: int) -> ListNode:
    def rotate(head):
        cur = head
        while cur.next.next:
            cur = cur.next
        tmp = cur.next
        cur.next = None
        tmp.next = head
        return tmp
    
    if not head or not head.next:
        return head
    
    cur = head
    n = 0
    while cur:
        cur = cur.next
        n += 1
    
    for i in range(k % n):
        head = rotate(head)
    return head