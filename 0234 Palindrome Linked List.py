def isPalindrome(head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls == ls[::-1]

# fast and slow pointers
def isPalindrome(self, head: ListNode) -> bool:
    if not head:
        return True
    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    pre = None
    cur = slow.next
    slow.next = None
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    # pre <= head
    while pre:
        if head.val != pre.val:
            return False
        head = head.next
        pre = pre.next
    return True