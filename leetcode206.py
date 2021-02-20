'''
206. 反转链表
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        t = ListNode(0)
        t = t.next
        temp = head
        # 4->3->2->1
        while temp != None:
            node1 = temp.next #3->2->1 ---> 2->1  --> 1
            temp.next = t     #4   --> 4->3
            t = temp          #4   --> 4->3
            temp = node1      #3->2->1  --> 2->1
        return t


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a2.next = a1
a3.next = a2
a4.next = a3
# a4 = [4,3,2,1]
code206 = Solution()
print(code206.reverseList(a4).val)