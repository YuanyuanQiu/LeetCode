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


# fast and slow pointers
def isPalindrome(self, head: ListNode) -> bool:
    if not head or not head.next:
        return True
    fast, slow = head, head
    half = []
    while fast and fast.next:
        half.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if not half:
            return False
        if slow.val != half.pop():
            return False
        slow = slow.next
    return True