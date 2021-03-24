def isPalindrome(head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls == ls[::-1]