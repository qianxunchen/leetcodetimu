'''
整数转罗马
'''
#贪心
class Solution:
    def intToRoman(self, num):
        N = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        for key in n:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res = res + N[n.index(key)] * count
                num = num % key
        return res

code12 = Solution()
print(code12.intToRoman(4001))