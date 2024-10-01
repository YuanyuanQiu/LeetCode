def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    if not head:
        return
    # 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
    dic = {}
    cur = head
    while cur:
        dic[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    # 构建新节点的 next 和 random 指向
    while cur:
        dic[cur].next = dic.get(cur.next)
        dic[cur].random = dic.get(cur.random)
        cur = cur.next
    # 返回新链表的头节点
    return dic[head]