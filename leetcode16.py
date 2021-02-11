'''
最接近的三数之和
'''
class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        lenght = len(nums)
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = lenght - 1 #最右元素
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - res):
                    res = total
                    while l < r and nums[l] == nums[l + 1]: #判断与下一元素是否相同
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                if total > target:
                    r = r - 1
                elif total < target:
                    l = l + 1
                else:
                    return res
        return res

code16 = Solution()
print(code16.threeSumClosest([-1,2,1,-4],1))
