'''
32. 最长有效括号
'''
class Solution:
    def longestValidParentheses(self, s):
        lenght = len(s)
        if lenght < 2:
            return 0

        res = 0
        temp = []
        for i in range(lenght):
            if s[i] == "(" or len(temp) == 0 or s[temp[-1]] == ")": #栈顶为）时任何符号都无法消除，所以可以入栈
                temp.append(i)
            else:
                temp.pop()
                res = max(res, i-(temp[-1] if temp else -1))

        return res


code = Solution()
print(code.longestValidParentheses("(()"))
print(code.longestValidParentheses(")()())"))
print(code.longestValidParentheses(")("))


