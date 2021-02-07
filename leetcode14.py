'''
最长公共前缀
'''

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        temp = 0
        if len(strs) == 0:
            return res
        min_str = strs[0]
        for x in strs:
            if len(x) <= len(min_str):
                min_str = x
        for i in range(len(min_str)):
            for str in strs:
                if str[i] != min_str[i]:
                    temp = 1
                else:
                    pass
            if temp == 0:
                res = res + min_str[i]
        return res


code14 = Solution()
print(code14.longestCommonPrefix([]))


