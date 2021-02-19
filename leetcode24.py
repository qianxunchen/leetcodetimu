'''
24. 两两交换链表中的节点
'''
#递归

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
            res = ListNode(0)
            temp = head
            def jiaohuan(temp,res):
                if not temp or not temp.next:
                    return temp
                res = temp.next
                # 把剩下的进行下一次循环
                temp.next = jiaohuan(res.next,res)
                res.next = temp
                return res
            new = jiaohuan(temp,res)
            return new

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a2.next = a1
a3.next = a2
a4.next = a3
# a4 = [4,3,2,1]
code24 = Solution()
print(code24.swapPairs(a4).val)

#迭代

# # # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#             res = ListNode(0)
#             res.next = head
#             temp = res
#             while temp.next and temp.next.next:
#                 # 节点1
#                 node1 = temp.next
#                 # 2
#                 node2 = temp.next.next
#                 # 交换，此时temp第一个是0
#                 temp.next = node2
#                 # 把没有交换过的接上去
#                 node1.next = node2.next
#                 node2.next = node1
#                 # 交换后temp的第一个是一开始的node1
#                 temp = node1
#             return res.next
#
# a1 = ListNode(1)
# a2 = ListNode(2)
# a3 = ListNode(3)
# a4 = ListNode(4)
# a2.next = a1
# a3.next = a2
# a4.next = a3
# # a4 = [4,3,2,1]
# code24 = Solution()
# print(code24.swapPairs(a4).val)