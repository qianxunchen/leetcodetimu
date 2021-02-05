'''
盛水最多的容器
'''
class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_water = 0
        while i < j:
            if height[i] < height[j]:
                max_water = max(max_water, (height[i] * (j-i)))
                i = i + 1
            else:
                max_water = max(max_water, (height[j] * (j-i)))
                j = j - 1

        return max_water

code11 = Solution()
print(code11.maxArea([1,8,6,2,5,4,8,3,7]))