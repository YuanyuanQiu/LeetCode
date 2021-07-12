def middleNode(self, head: ListNode) -> ListNode:
    if not head:
        return head
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if not fast or not fast.next:
        return slow
    else:
        return slow.next