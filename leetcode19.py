'''
删除链表的倒数第 N 个结点
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenght = 0
        #链表只能用一次，需要给另一个链表用来删节点
        head1 = head
        while head != None:
            # print(head.val)
            head = head.next
            lenght += 1

        temp = []
        for i in range(lenght):
            if i != (lenght-n):
                temp.append(head1.val)
            head1 = head1.next

        ResIsNull = ListNode(0)
        ResIsNull = ResIsNull.next
        if len(temp) == 0:
            return ResIsNull

        r1 = ListNode(temp[0])
        res = r1
        r2 = r1
        for i in temp[1:]:
            data = ListNode(i)
            r2.next = data
            r2 = r2.next
        return res


a1 = ListNode(1)

#创建链表的方法
# a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(3)
# a3.next = a2
# a2.next = a1

code19 = Solution()
print(code19.removeNthFromEnd(a1, 1).val)