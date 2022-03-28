class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        dummy = None
        move1, move2 = dummy, head
        temp = set()

        while move2:
            if move2.val not in temp:
                temp.add(move2.val)
                move1 = move2

            else:
                move1.next = move2.next

            move2 = move2.next

        return head
