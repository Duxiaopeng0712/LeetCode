class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    def reverseMN(start: ListNode):
        pre, current = None, start
        while current:
            temp = current.next
            current.next = pre
            pre.next = current
            current.next = temp

        dummy = None
        dummy.next = head
        start = dummy

        for i in range(left - 1):
            start = start.next

        end = start
        for j in range(right - left + 1):
            end = end.next

        left_s = start.next
        right_s = end.next

        start.next = None
        end.next = None

        reverseMN(left_s)
        pre.next = end.next
        start.next = right_s

        return dummy.next
