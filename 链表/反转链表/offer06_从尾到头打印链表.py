# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(head: ListNode) -> List[int]:
        dummy, cur = None, head
        res = []

        while cur:
            temp = cur.next
            cur.next = dummy
            dummy = cur
            cur = temp

        while dummy:
            res.append(dummy.val)
            dummy = dummy.next

        return res


if __name__ == '__main__':
    node1 = ListNode(0)
    p = node1
    for i in range(1, 11):
        tmp = ListNode(i)
        p.next = tmp
        p = p.next

    res = Solution.reversePrint(node1.next)

    print(res)
