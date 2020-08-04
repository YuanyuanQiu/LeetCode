# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
def reverseList(self, head: ListNode) -> ListNode:
    pre = None # 当前节点的前驱节点
    cur = head # 当前遍历到的节点
    while cur:
        temp = cur.next   # 先把原来cur.next位置存起来
        cur.next = pre
        pre = cur
        cur = temp
    return pre