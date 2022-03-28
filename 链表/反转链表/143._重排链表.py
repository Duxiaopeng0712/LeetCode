class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return

        slow, fast = head, head
        #  找中点，链表分为两个
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        newhead = slow.next
        slow.next = None

        # 第二个链表反转
        newhead = Solution.reverse(newhead)

        while newhead:
            temp = newhead.next
            newhead.next = head.next
            head.next = newhead
            head = newhead.next
            newhead = temp

    def reverse(self, head: ListNode):
        first = None
        second = head

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        return first

