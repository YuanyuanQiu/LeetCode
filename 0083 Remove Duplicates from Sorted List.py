# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)

node1.next = node2
node2.next = node3

# def printList(node):
#     while node:
#         print(node.val)
#         node = node.next

# printList(node1)

head = node1

def deleteDuplicates(head):
    node = head
    
    # 不为空链表和最后一个node
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    
    # head是头节点，位置没变，node做了引用，用node做了链表的操作
    return head

def deleteDuplicates(head):
    if not (head and head.next):
        return head
    i = head
    j = head.next
    while j:
		# 如果i不等于j，则i前进一位，然后将j的值赋给i
        if i.val!=j.val:
            i = i.next
            i.val = j.val # 将i的下一位赋值与i不同的j值
        # 不管i是否等于j，j每次都前进一位
        j = j.next
    i.next = None
    return head

print(deleteDuplicates(head))