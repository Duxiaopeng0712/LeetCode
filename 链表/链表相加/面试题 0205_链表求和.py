class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        node = head
        remaining = 0
        while l1 or l2:
            if l1 == None:
                node.next = l2
                l1 = ListNode(0)
            if l2 == None:
                node.next = l1
                l2 = ListNode(0)
            remaining = l1.val + l2.val
            node.next = ListNode(remaining % 10)
            remaining = remaining // 10
            node = node.next
            l1 = l1.next
            l2 = l2.next
        if remaining:
            node.next = ListNode(remaining)
        return head.next

