class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        move = head
        while move:
            if move.val == move.next.val:
                move.next = move.next.next

            move = move.next

        return dummy.next

