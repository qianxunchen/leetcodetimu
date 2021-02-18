'''
有效括号的生成
'''
#暴力法，先生成，再检验
# class Solution:
#     def generateParenthesis(self, n):
#         def generate(temp):
#             if len(temp) == 2 * n:
#                 if isValid(temp):
#                     res.append(temp)
#             else:
#                 temp = temp + "("
#                 generate(temp)
#                 temp = temp[:-1]
#                 temp = temp + ")"
#                 generate(temp)
#                 temp = temp[:-1]
#
#         def isValid(s):
#             # 单数一定是无效的
#             temp = []
#             pair1 = ["(", "[", "{"]
#             pair2 = [")", "]", "}"]
#             for i in s:
#                 if i in pair1:
#                     temp.append(i)
#                 elif i in pair2:
#                     if len(temp) == 0:
#                         return False
#                     if temp[-1] == pair1[pair2.index(i)]:
#                         temp.pop()
#                     else:
#                         return False
#             if len(temp) != 0:
#                 return False
#             else:
#                 return True
#
#
#         res = []
#         temp = ""
#         generate(temp)
#         return res
#
#
# code22 = Solution()
# print(code22.generateParenthesis(1))


class Solution:
    def generateParenthesis(self, n):
        res = []
        return res


code22 = Solution()
print(code22.generateParenthesis(1))

