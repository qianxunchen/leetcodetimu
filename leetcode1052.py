'''
1052. 爱生气的书店老板
'''
class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        grulen = len(grumpy)
        res = 0
        max_temp = 0
        for i in range(grulen):
            if grumpy[i] == 0:
                res = res+customers[i]
                customers[i] = 0
        for x in range(grulen):
            if sum(customers[x:x+X]) > max_temp:
                max_temp = sum(customers[x:x+X])
        res = res+max_temp
        return res

code = Solution()
print(code.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3))


