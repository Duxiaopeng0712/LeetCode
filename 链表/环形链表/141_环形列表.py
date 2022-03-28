from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = set()

        move = ListNode(0)
        move.next = head

        while move:
            if move in temp:
                return True
            temp.add(move)
            move = move.next
        return False
