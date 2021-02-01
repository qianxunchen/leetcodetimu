'''
整数反转
'''
class Solution:
    def reverse(self, x):
        fushu = 0
        set_x = 0
        if x == 0:
            return 0
        if 0 < x < 10 or -10 < x < 0:
            return x
        if x < 0 :
            x = -x
            fushu = 1
        while x != 0:
            set_x = set_x * 10 + x % 10
            x = x // 10

        if fushu == 1:
            set_x = -set_x
        if -2**31 > set_x or set_x > (2**31 -1):
            return 0
        else:
            return set_x



code7 = Solution()
print(code7.reverse(1534236469))
