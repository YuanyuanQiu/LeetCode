# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
def reverseList(self, head: ListNode) -> ListNode:
    pre = None # 前驱节点
    cur = head # 当前节点
    while cur:
        temp = cur.next   # 先把原来cur.next位置存起来
        cur.next = pre # 反转
        pre = cur # 前驱节点指针后移一位
        cur = temp # 当前节点指针后移一位
    return pre