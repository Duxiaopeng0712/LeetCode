class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(self, head: ListNode):

    first = None
    second = head

    while second:
        temp = second.next
        second.next = first
        first = second
        second = temp

    return first

