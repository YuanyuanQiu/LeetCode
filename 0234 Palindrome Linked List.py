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


def isPalindrome(self, head: ListNode) -> bool:
    vals = []
    current_node = head
    while current_node is not None:
        vals.append(current_node.val)
        current_node = current_node.next
    return vals == vals[::-1]