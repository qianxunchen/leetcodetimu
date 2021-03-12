'''
56. 合并区间
'''
class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)
        lenght = len(intervals)
        if lenght <= 1:
            return intervals
        res = []
        for i in intervals:
            if not res or res[-1][-1] < i[0]:
                res.append(i)
            else:
                end = max(res[-1][-1], i[-1])
                res[-1][1] = end
        return res


code = Solution()
print(code.merge([[1,3],[2,6],[8,10],[15,18]]))
print(code.merge([[1,3],[2,6],[8,10],[9,18]]))
print(code.merge([[1,4],[0,4]]))
print(code.merge([[1,4],[0,1]]))
print(code.merge([[1,4],[0,0]]))
print(code.merge([[1,4],[0,2],[3,5]]))