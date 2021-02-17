'''
21. 合并两个有序链表
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #：链表转列表
        temp1 = []
        temp2 = []
        while l1 != None:
            temp1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            temp2.append(l2.val)
            l2 = l2.next
        # 链表为空的情况
        ResIsNull = ListNode(0)
        ResIsNull = ResIsNull.next
        if len(temp1) == 0 and len(temp2) == 0 :
            return ResIsNull

        temp = temp1 + temp2
        #冒泡排序
        lenght = len(temp)
        for i in range(lenght-1):
            for x in range(lenght-i-1):
                if temp[x] > temp[x+1]:
                    temp[x], temp[x+1] = temp[x+1], temp[x]
        print(temp)
        r1 = ListNode(temp[0])
        res = r1
        r2 = r1
        for i in temp[1:]:
            data = ListNode(i)
            r2.next = data
            r2 = r2.next
        return res



a1 = ListNode(0)
a2 = ListNode(2)
a3 = ListNode(1)
a3.next = a2
a2.next = a1

b1 = ListNode(4)
b2 = ListNode(5)
b3 = ListNode(6)
b3.next = b2
b2.next = b1

code21 = Solution()
print(code21.mergeTwoLists(a3,b3).val)

