class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(next=head)
        h = dummy

        tem = ListNode()
        t = tem

        while dummy.next:
            if dummy.next.val >= x:
                tem.next = ListNode(dummy.next.val)
                tem = tem.next
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        else:
            dummy.next = t.next
            return h.next


"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。

"""
