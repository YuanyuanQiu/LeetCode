def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return head
    pre = ListNode(val=0, next=head)
    dummy = pre
    while head:
        if head.val == val:
            pre.next = head.next
            head = head.next
        else:
            pre = pre.next
            head = head.next
    return dummy.next


# 递归
def removeElements(self, head, val):
    if not head:
        return head
    head.next = self.removeElements(head.next, val)
    return head if head.val != val else head.next