class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # 两个空指针，一个用于遍历、一个用于指向新链表
        p = q = ListNode(None)
        # 进位：无进位为0，有进位为1
        flag = 0
        while l1 or l2 or flag:
            # 相加
            flag += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            # 将当前计算的值存储
            p.next = ListNode(flag % 10)
            # p指向下一个下一个节点
            p = p.next
            # 计算是否有进位flag
            flag = flag // 10
            # l1、l2后移
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return q.next
