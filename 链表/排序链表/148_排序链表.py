# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# 快速排序
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        # 分成三个链表，分别是比轴心数小，相等，大的数组成的链表
        big = None
        small = None
        equal = None
        cur = head
        while cur is not None:
            t = cur
            cur = cur.next
            if t.val < head.val:
                t.next = small
                small = t
            elif t.val > head.val:
                t.next = big
                big = t
            else:
                t.next = equal
                equal = t

        # 拆完各自排序即可，equal 无需排序
        big = self.sortList(big)
        small = self.sortList(small)

        ret = ListNode(None)
        cur = ret

        # 将三个链表组合成一起，这一步复杂度是 o(n)
        # 可以同时返回链表的头指针和尾指针加速链表的合并。
        for p in [small, equal, big]:
            while p is not None:
                cur.next = p
                p = p.next
                cur = cur.next
                cur.next = None
        return ret.next
