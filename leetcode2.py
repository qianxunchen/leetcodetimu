'''
两数相加
'''
# Definition for singly-linked list.
# 定义单链表的类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1,l2):
        self.l1 = l1
        self.l2 = l2
        l3 = []
        len_1 = len(l1)
        len_2 = len(l2)
        max_12 = max(len_1,len_2)
        for i in range(max_12):
            if len(l3) != i+1:
                l3.append(0)
            if i+1 > len_1:
                sum = l2[i]
            elif i+1 > len_2:
                sum = l1[i]
            else:
                sum = l1[i]+l2[i]
            if sum >= 10:
                l3.append(0)
                l3[i] = l3[i] + sum % 10
                l3[i+1] = 1
                if l3[i] >= 10:
                    l3[i] = l3[i] % 10
                    l3[i+1] = l3[i+1]+1
            else:
                l3[i] = l3[i] + sum
                if l3[i] >= 10:
                    l3[i] = l3[i] % 10
                    l3.append(1)


        # 创建头结点
        head = ListNode(l3[0])
        # 头结点
        r = head
        # 指针
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in l3[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r


q = Solution()
# print(q.addTwoNumbers([2,4,3],  [5,6,4]))
print(q.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]).val)


'''
    以下是提交的代码 
    
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         ll1 = []
#         head=l1
#         temp=head
#         while temp!=None:
#             ll1.append(temp.val)
#             temp=temp.next
#
#         ll2 = []
#         head=l2
#         temp=head
#         while temp!=None:
#             ll2.append(temp.val)
#             temp=temp.next
#
#         l3 = []
#         len_1 = len(ll1)
#         len_2 = len(ll2)
#         max_12 = max(len_1,len_2)
#         for i in range(max_12):
#             if len(l3) != i+1:
#                 l3.append(0)
#             if i+1 > len_1:
#                 sum = ll2[i]
#             elif i+1 > len_2:
#                 sum = ll1[i]
#             else:
#                 sum = ll1[i]+ll2[i]
#             if sum >= 10:
#                 l3.append(0)
#                 l3[i] = l3[i] + sum % 10
#                 l3[i+1] = 1
#                 if l3[i] >= 10:
#                     l3[i] = l3[i] % 10
#                     l3[i+1] = l3[i+1]+1
#             else:
#                 l3[i] = l3[i] + sum
#                 if l3[i] >= 10:
#                     l3[i] = l3[i] % 10
#                     l3.append(1)
#
#         # 创建头结点
#         head = ListNode(l3[0])
#         # 头结点
#         r = head
#         # 指针
#         p = head
#         # 逐个为 data 内的数据创建结点, 建立链表
#         for i in l3[1:]:
#             node = ListNode(i)
#             p.next = node
#             p = p.next
#         return r

