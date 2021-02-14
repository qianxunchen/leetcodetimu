'''
17. 电话号码的字母组合
'''

class Solution:
    def letterCombinations(self, digits):
        res = []
        temp = []
        lenght = len(digits)
        if lenght == 0:
            return res

        s = [['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']]

        for i in range(lenght):
            temp.append(s[int(digits[i])-2])
        res = temp[0]
        for a in range(1,len(temp)):
            ttemp = []
            for x in res:
                for xx in temp[a]:
                    ttemp.append(x+xx)
            res = ttemp
        return res


code17 = Solution()
print(code17.letterCombinations("234"))
print(code17.letterCombinations(""))





