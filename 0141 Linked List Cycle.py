def hasCycle(self, head: ListNode) -> bool:
    if head is None:
        return False
    dic = {}
    cur = head
    while True: 
        # 下一个数已存在于字典中
        if dic.get(cur.next) is not None:
            return True

        # 存入字典
        dic[cur] = 1

        # 遍历下一个
        cur = cur.next

        # 遍历到结尾
        if cur is None:
            return False