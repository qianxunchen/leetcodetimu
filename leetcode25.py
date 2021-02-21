'''
25. K 个一组翻转链表
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverList(start, end):
            t = ListNode(0)
            t = t.next
            temp = start
            # 4->3->2->1
            while temp != end:
                node1 = temp.next  # 3->2->1 ---> 2->1  --> 1
                temp.next = t  # 4   --> 4->3
                t = temp  # 4   --> 4->3
                temp = node1  # 3->2->1  --> 2->1
            return t
        def cut_nums(head, k):
            lenght = 0
            temp2 = head
            while temp2:
                temp2 = temp2.next
                lenght += 1
            if lenght < k:
                return head

            res = ListNode(0)
            res.next = head
            temp3 = res
            while head:
                end = head
                for _ in range(k):
                    if not end:
                        return res.next
                    end = end.next
                newhead = reverList(head, end)
                temp3.next = newhead
                head.next = end

                temp3 = head
                head = end
            return res.next

        res = cut_nums(head,k)
        return res









a1 = ListNode(5)
a2 = ListNode(4)
a3 = ListNode(3)
a4 = ListNode(2)
a5 = ListNode(1)
a2.next = a1
a3.next = a2
a4.next = a3
a5.next = a4
# a4 = [4,3,2,1]
code25 = Solution()
aa = code25.reverseKGroup(a5,2)
while aa:
    print(aa.val)
    aa = aa.next