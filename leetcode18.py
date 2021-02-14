'''
四数之和
'''
class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        lenght = len(nums)
        res = []
        if lenght < 4:
            return res
        if lenght == 4:
            if sum(nums) == target:
                res.append(nums)
                return res
            else:
                return res
        for start1 in range(lenght-3):
            nums2 = nums[start1 + 1:]
            # print(nums2)
            for i in range(len(nums2) - 2):
                if i > 0 and nums2[i] == nums2[i - 1]:
                    continue
                l = i + 1
                r = len(nums2) - 1  # 最右元素
                while l < r:
                    total = nums[start1] + nums2[i] + nums2[l] + nums2[r]
                    if total == target:
                        if [nums[start1], nums2[i], nums2[l], nums2[r]] not in res:
                            res.append([nums[start1], nums2[i], nums2[l], nums2[r]])
                            while l < r and nums2[l] == nums2[l + 1]:  # 判断与下一元素是否相同
                                l += 1
                            while l < r and nums2[r] == nums2[r - 1]:
                                r -= 1
                        l += 1
                        r -= 1
                    if total < target:
                        l = l + 1
                    if total > target:
                        r = r - 1
        return res




code15 = Solution()
# print(code15.fourSum([1, 0, -1, 0, -2, 2],0))
# print(code15.fourSum([-3,-1,0,2,4,5],0))
# print(code15.fourSum([-2,0,1,1,2],0))
# print(code15.fourSum([0,0,0,0],1))
# print(code15.fourSum([-2,-1,-1,1,1,2,2],0))
# print(code15.fourSum([-3,-1,0,2,4,5],2))
# print(code15.fourSum([-5,-4,-3,-2,-1,0,0,1,2,3,4,5],0))
# print(code15.fourSum([1,-2,-5,-4,-3,3,3,5],-11))
# print(code15.fourSum([-1,0,1,2,-1,-4],-1))
# print(code15.fourSum([-1,-5,-5,-3,2,5,0,4],-7))
print(code15.fourSum([1,0,-1,0,-2,2],0))