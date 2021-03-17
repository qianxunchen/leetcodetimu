'''
35. 搜索插入位置
'''
# 暴力法
class Solution:
    def searchInsert(self, nums, target):
        lenght = len(nums)
        if target <= nums[0]:
            return 0
        for i in range(lenght):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                continue
            elif nums[i] > target:
                return i

        return lenght



code = Solution()
print(code.searchInsert([1,3,5,6], 5))
print(code.searchInsert([1,3,5,6], 2))
print(code.searchInsert([1,3,5,6], 7))
print(code.searchInsert([1,3,5,6], 0))
print(code.searchInsert([1], 0))
print(code.searchInsert([1,3], 2))

