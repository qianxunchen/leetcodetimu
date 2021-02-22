'''
27. 移除元素
'''
class Solution:
    def removeElement(self, nums, val):
        nums.sort()
        lenght = len(nums)
        res = 0
        for i in range(lenght):
            if nums[res] == val:
                nums.append(nums[res])
                nums.pop(res)
            else:
                res += 1
        return nums,res

code26 = Solution()
print(code26.removeElement([1,2,3,4,4,3],3))

