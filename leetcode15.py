'''
三数之和
'''
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        lenght = len(nums)
        res = []
        if len(nums) <= 2:
            return res
        for i in range(len(nums)-2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = lenght - 1 #最右元素
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: #判断与下一元素是否相同
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                if total < 0:
                    l = l + 1
                if total > 0:
                    r = r - 1
        return res

code15 = Solution()
print(code15.threeSum([-1,0,1,2,-1,-4]))
print(code15.threeSum([0]))
print(code15.threeSum([-2,0,1,1,2]))


# 提交超时
# class Solution:
#     def threeSum(self, nums):
#         nums = sorted(nums)
#         res = []
#         if len(nums) <= 2:
#             return res
#
#         for i in range(len(nums)-2):
#             if nums[i] > 0:
#                 return res
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             nums_1 = nums[i+1:]
#             for n in range(len(nums_1)-1):
#                 nums_2 = nums_1[n + 1:]
#                 for x in range(len(nums_2)):
#                     if nums[i] + nums_1[n] + nums_2[x] == 0:
#                         if [nums[i], nums_1[n], nums_2[x]] not in res:
#                             res.append([nums[i], nums_1[n], nums_2[x]])
#         return res
#
#
# code15 = Solution()
# print(code15.threeSum([-1,0,1,2,-1,-4]))
# print(code15.threeSum([0]))
# print(code15.threeSum([-2,0,1,1,2]))