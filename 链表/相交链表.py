class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Code:
    def main(self):
        headA = ListNode(4)
        tmp1 = ListNode(1)
        headA.next = tmp1
        tmp2 = ListNode(8)
        tmp1.next = tmp2
        tmp3 = ListNode(4)
        tmp2.next = tmp3
        tmp4 = ListNode(5)
        tmp3.next = tmp4

        headB = ListNode(5)
        tmp5 = ListNode(6)
        headB.next = tmp5
        tmp6 = ListNode(1)
        tmp5.next = tmp6
        tmp6.next = tmp2

        res = self.getIntersectionNode(headA, headB)
        print(res.val)

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        moveA, moveB = headA, headB
        lenA, lenB = 0, 0
        cost = 0
        while moveA:
            moveA = moveA.next
            lenA += 1
        while moveB:
            moveB = moveB.next
            lenB += 1
        moveA, moveB = headA, headB
        if lenA >= lenB:
            cost = lenA - lenB
            moveA = self.move(headA, cost)
        else:
            cost = lenB - lenA
            moveB = self.move(headB, cost)
        while moveA != moveB and moveA != None:
            moveA = moveA.next
            moveB = moveB.next
        return moveA

    def move(self, head: ListNode, cost) -> ListNode:
        for i in range(cost):
            head = head.next
        return head


test = Code()
Code.main(test)
