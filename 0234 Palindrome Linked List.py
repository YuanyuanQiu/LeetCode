def isPalindrome(head):
    ls = []
    while head != None:
        ls.append(head.val)
        head = head.next

    if len(ls)<=1:
        return True
        
    n = len(ls)//2
    if ls[:n] == ls[-1*n:][::-1]:
        return True
    else:
        return False


def isPalindrome(head):
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    return ls == ls[::-1]