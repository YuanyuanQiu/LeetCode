def hasCycle(self, head: ListNode) -> bool:
    seen = set()
    while head:
        if head in seen:
            return True
        seen.add(head)
        head = head.next
    return False


def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
        return False
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False