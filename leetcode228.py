'''
228. 汇总区间
'''
class Solution:
    def summaryRanges(self, nums):
        lenght = len(nums)
        res = []
        if lenght == 1:
            return [str(nums[0])]
        if lenght == 0:
            return res

        # 区间头节点
        start = nums[0]
        for i in range(lenght-1):
            if nums[i]+1 == nums[i+1]:
                if nums[i+1] == nums[-1]:
                    res.append(str(start)+"->"+str(nums[i+1]))
                continue
            else:
                end = nums[i]
                if start == end:
                    res.append(str(start))
                    start = nums[i + 1]
                else:
                    temp = str(start)+"->"+str(end)
                    res.append(temp)
                    start = nums[i + 1]
        if nums[-1]-1 != nums[-2]:
            res.append(str(nums[-1]))
        return res

code = Solution()
print(code.summaryRanges([0,2,3,4,6,8,9]))
print(code.summaryRanges([0,1,2,4,5,7]))
print(code.summaryRanges([]))
print(code.summaryRanges([-1]))

