from jinja2.nodes import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(self, lists: list[ListNode]):
    result = None
    for i in range(len(lists)):
        result = mergeTwoLists(result, lists[i])

    return result


def mergeTwoLists(list1: ListNode, list2: ListNode):
    # 1、设置空指针，返回的链表为空指针指向的下一个结点
    dummy = ListNode(0)
    # 2、设置移动指针,始终指向新链表的最后一个结点
    move = dummy
    # 3、移动指针
    while list1 and list2:
        if list1.val < list2.val:
            move.next = list1
            list1 = list1.next
        else:
            move.next = list2
            list2 = list2.next
        move = move.next
    move.next = list1 if list1 else list2
    return dummy.next
