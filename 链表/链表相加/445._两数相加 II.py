
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        def listnode2stack(node):  # 将链表转换为各位的数字并压入栈中，返回一个 stack,栈底为数字的高位，栈顶为数字的低位
            res = []
            while node:
                res.append(node.val)
                node = node.next
            return res

        stack1, stack2 = listnode2stack(l1), listnode2stack(l2)
        remaining = 0  # 存储 10 进制下进位数
        dummynode = ListNode()  # 创建一个 dummynode，链表通常都需要创建一个 dummynode
        while stack1 != [] or stack2 != [] or remaining != 0:  # 当 stack 或进位数不为空
            tmp_sum = remaining  # 定义 tmp_sum 为某一位数上累计的值
            # 栈顶为数字的低位，如果有则累加到这一位对应的 tmp_sum 中
            if stack1 != []:
                tmp_sum += stack1.pop()
            if stack2 != []:
                tmp_sum += stack2.pop()
            new_node = ListNode(tmp_sum % 10)  # 创建新节点存储当前位的数字，由于存在进位，所以新节点的值为 tmp_sum 对 10 取余数
            remaining = tmp_sum // 10  # 更新 remainging,即进到下一高位的值，即 tmp 对 10 的商
            new_node.next = dummynode.next  # 将新节点的 next 指向 dummynode 的 next
            dummynode.next = new_node  # 更新 dummynode 的 next 让它指向新节点
        return dummynode.next


