class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n):
    # 1、定义空指针，并指向头节点
    dummy = ListNode(0)
    dummy.next = head
    # 2、定义快慢指针
    slow, fast = dummy, dummy
    # 3、快指针先走n步
    for i in range(n):
        fast = fast.next
    # 4、快慢指针同时走
    while fast and fast.next:
        slow, fast = slow.next, fast.next
    # 5、删除倒数第n个结点
    slow.next = slow.next.next
    # 6、返回头节点
    return dummy.next





