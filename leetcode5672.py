'''
是否为有序数组轮转
'''
# class Solution:
#     def check(self, nums):
#         # 我们称数组A在轮转x个位置后得到长度相同的数组B ，当它们满足A[i] == B[(i + x) % A.length] ，其中 % 为取余运算。
#         # A 是排序好的，B是轮转后的
#         # temp：轮转几次
#         temp = None
#         sortnums = sorted(nums)
#         if len(nums) == 2 or nums == sortnums:
#             return True
#         for i in range(len(nums)):
#             if sortnums[0] == nums[(0+i) % len(sortnums)]:
#                 temp = i
#
#         print(temp)
#         if temp != None:
#             for x in range(len(sortnums)):
#                 if sortnums[x] != (nums[(x+temp) % len(nums)]):
#                     print(sortnums[x])
#                     print(nums[(x+temp) % len(nums)])
#                     return False
#             else:
#                 return True
#         else:
#             return False
#
# code5672 = Solution()
# print(code5672.check([7,9,1,1,1,3]))
# # print(code5672.check([2,1,3,4]))
# # print(code5672.check([3,4,5,1,2]))

class Solution:
    def check(self, nums):
        temp = None
        sortnums = sorted(nums)
        if len(nums) == 2 or nums == sortnums:
            return True
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                temp = i

        if temp != None:
            nums_sort = nums[temp:]+nums[:temp]
            if nums_sort == sortnums:
                return True
            else:
                return False
        else:
            return False


code5672 = Solution()
print(code5672.check([7,9,1,1,1,3]))
print(code5672.check([2,1,3,4]))
print(code5672.check([3,4,5,1,2]))



