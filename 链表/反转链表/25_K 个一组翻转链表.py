from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(self, head: Optional[ListNode], k: int):
    def reverderMNGroup(start, end):
        pre, current = None, start
        while current != end:
            temp = current.next
            current.next = pre
            pre.next = current
            current.next = temp
        return pre

    start, end = head, head
    for _ in range(k):
        if not end:
            return head
        else:
            end = end.next
    res = reverseKGroup(start, end)
    start.next = self.rereverseKGroup(end, k)
    return res
