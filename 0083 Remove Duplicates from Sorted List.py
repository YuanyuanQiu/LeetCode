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

print(deleteDuplicates(head))