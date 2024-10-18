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

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # number of nodes = 0
    if not head or k == 0:
        return head
    
    # number of nodes
    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1
    
    # edge cases
    k = k % n
    if k == 0:
        return head

    # move fast to create the gap
    slow, fast = head, head
    while k > 0:
        fast = fast.next
        n 
        k -= 1
    # move fast to the last node of the linked list; move slow to the node before new head
    while fast.next:
        slow = slow.next
        fast = fast.next
    new_head = slow.next
    slow.next = None
    fast.next = head
    return new_head