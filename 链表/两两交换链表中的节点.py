class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 1、虚拟结点
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current and current.next and current.next.next:
            first = current
            second = current.next
            third = current.next.next

            first.next = third
            second.next = third.next
            third.next = second

            current = current.next.next

        return dummy.next




