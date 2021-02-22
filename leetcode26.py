'''
26. 删除排序数组中的重复项
'''
#快慢指针
class Solution:
    def removeDuplicates(self, nums):
        nums.sort()
        lenght = len(nums)
        res = 0
        for i in range(1, lenght):
            # print(nums[i])
            if nums[res] == nums[i]:
                continue
            else:
                nums[res+1] = nums[i]
                res += 1
        return nums,res+1



code26 = Solution()
print(code26.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(code26.removeDuplicates([1,1,2]))

