class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        dummy = ListNode(0)
        dummy = head

        while dummy is not None:
            temp.append(dummy.val)
            dummy = dummy.next

        return temp == temp[::-1]
