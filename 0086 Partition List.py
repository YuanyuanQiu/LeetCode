# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # pre node of small linked list
        dummy1 = ListNode()
        # pre node of large linked list
        dummy2 = ListNode()
        # current node in each linked list
        cur, cur1, cur2 = head, dummy1, dummy2
        while cur:
            # less than x
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            # greater than or equal to x
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        cur1.next = dummy2.next
        # 没有这一句会成环
        '''
        假设链表是4->1->2->3，然后x是4，第一次判断head.val和x关系后，big指向值为4的节点, 而值为4的结点指向值为1的结点。
        如果你不改变big.next的指向的话，它就一直指向值为1的结点，最后small_dummy为1->2->3，big_dummy为4->1->2->3，
        进行连接就成了环。
        '''
        cur2.next = None
        return dummy1.next
        