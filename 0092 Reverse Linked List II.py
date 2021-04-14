def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    dummy_node = ListNode(-1)
    dummy_node.next = head
    pre = dummy_node
    for _ in range(left - 1):
        pre = pre.next

    cur = pre.next
    for _ in range(right - left):
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = pre.next
        pre.next = tmp
    return dummy_node.next