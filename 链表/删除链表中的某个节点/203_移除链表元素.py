class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def main(self):
        head = ListNode(7)
        tmp1 = ListNode(7)
        head.next = tmp1
        tmp2 = ListNode(7)
        tmp1.next = tmp2
        tmp3 = ListNode(7)
        tmp2.next = tmp3

        Solution.removeElements(head=head, val=7)

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        move = dummy

        while move.next:
            if move.next.val == val:
                move.next = move.next.next
            else:
                move = move.next
        return dummy.next
