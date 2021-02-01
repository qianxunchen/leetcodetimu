'''
最长回文子串
'''

class Solution:
    def longestPalindrome(self, s):
        lenght_str = len(s)
        # 记录当前回文串长度
        len_str = 1
        # 回文串起止点
        start, end = 0,0
        if lenght_str < 2:
            return s
        if lenght_str == 2 and s[0] != s[1]:
            return s[0]
        if lenght_str == 2 and s[0] == s[1]:
            return s
#       生成一个二维数组来存放各子串是否是回文串的结果，
#       其中行表示子串的第一个字符在字符串的位置，列表示子串的最后一个字符在字符串的位置
        dp = [[0]*lenght_str for _ in range(lenght_str)]
#       开始切分字符串，实际上并没有切割，只是比较各子串是否是回文串，是就在二维表中记录下起始位置
#       因为二维表的对角线位置肯定是同一个字符，所以不需要比较，从1开始
        for i in range(lenght_str):
            dp[i][i] = 1
        for j in range(1,lenght_str):
#             只需要二维表对角线的一半就可以计算出所有子串的情况
            for i in range(0, j):
                # 如果两个字符相同，那就判断他们之间的字符串是否为回文串
                if s[i] == s[j]:
                    # 子串为回文串
                    if j - i < 3:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[j][i] = 0

                if dp[i][j]:
                    if len_str < j - i + 1:
                        len_str = j - i + 1
                        start = i
        return s[start:start + len_str]


p = Solution()
print(p.longestPalindrome("abcda"))
