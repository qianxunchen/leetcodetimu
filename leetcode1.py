'''
两数之和
'''
class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums[i+1:]:
                x = nums[i+1:].index(a) + i +1
                return [i,x]


q = Solution()
print(q.twoSum([3,2,4],6))

