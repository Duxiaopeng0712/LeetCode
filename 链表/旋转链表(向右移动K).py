# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lens = 0
        dummy = ListNode(0)
        move, slow, fast = head, head, head

        # 1、获得链表长度
        while move:
            lens += 1
            move = move.next

        # 2、对长度取模（即向右移动的位数）
        if lens == 0 or lens == 1 or k == 0:
            return head
        pos = k % lens

        if pos == 0:
            return head
        # 3、fast先走post步：此时 slow 和 fast 之间的距离是 k；fast 指向第 k + 1 个节点
        for i in range(pos):
            fast = fast.next
        # 4、当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 5、dummy是倒数第 k 个节点，即新链表的头
        dummy = slow.next
        # 6、k和k+1结点断开连接
        slow.next = None
        # 7、最后一个结点指向头节点
        fast.next = head

        return dummy
