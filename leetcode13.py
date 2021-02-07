'''
罗马数字转整数
'''
class Solution:
    def romanToInt(self, s):
        sdict = {'M':1000, 'CM': 900, 'D': 500, 'CD': 400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX': 9, 'V':5, 'IV':4, 'I':1}
        res = 0
        stemp = s
        i = 0
        while i < len(stemp):
            if stemp[i:i+2] in sdict:
                res = res + sdict[stemp[i:i+2]]
                stemp = stemp[2:]
            else:
                res = res + sdict[stemp[i]]
                stemp = stemp[1:]
        return res


code13 = Solution()
print(code13.romanToInt("III"))

