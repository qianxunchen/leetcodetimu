'''
使用内置函数进行排序
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums2
        for i in nums1:
            nums.append(i)
        nums.sort()
        lenght = len(nums)
        if (lenght % 2) == 0:
            num1 = int(lenght / 2)
            num2 = num1 - 1
            tid = (nums[num1] + nums[num2]) / 2
        else:
            num1 = int(lenght / 2)
            tid = nums[num1]
        print(nums)
        return tid


code4 = Solution()
print(code4.findMedianSortedArrays([1,2],[3,4]))

'''
使用冒排序
'''
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         nums = nums2
#         for i in nums1:
#             nums.append(i)
#         lenght = len(nums)
#         for i in range(lenght-1):
#             for x in range(lenght-i-1):
#                 if nums[x] > nums[x+1]:
#                     nums[x], nums[x+1] = nums[x+1], nums[x]
#
#         if (lenght % 2) == 0:
#             num1 = int(lenght / 2)
#             num2 = num1 - 1
#             tid = (nums[num1] + nums[num2]) / 2
#         else:
#             num1 = int(lenght / 2)
#             tid = nums[num1]
#         print(nums)
#         return tid
#
#
# code4 = Solution()
# print(code4.findMedianSortedArrays([1,2],[3,4]))

