def deleteDuplicates(self, head: ListNode) -> ListNode:
    if not head:
        return head
    
    dummy = ListNode(0, head)

    cur = dummy
    while cur.next and cur.next.next:
        if cur.next.val == cur.next.next.val:
            x = cur.next.val
            while cur.next and cur.next.val == x:
                cur.next = cur.next.next
        else:
            cur = cur.next

    return dummy.next


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1, head)
    slow, fast = dummy, head
    # 是否处于重复中
    flag = False
    while fast and fast.next:
        # 有重复，移动fast直到最后一个重复值
        if fast.val == fast.next.val:
            flag = True
            fast = fast.next
        # 重复结束
        elif flag:
            slow.next = fast.next
            fast = slow.next
            flag = False
        # 没有重复
        else:
            slow = slow.next
            fast = fast.next
    if flag:
        slow.next = fast.next
    return dummy.next