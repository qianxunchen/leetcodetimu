'''
20. 有效的括号
'''
class Solution:
    def isValid(self, s: str) -> bool:
        #单数一定是无效的
        if len(s) % 2 == 1:
            return False
        temp = []
        pair1 = ["(", "[", "{"]
        pair2 = [")", "]", "}"]
        for i in s:
            if i in pair1:
                temp.append(i)
            elif i in pair2:
                if len(temp) == 0:
                    return False
                if temp[-1] == pair1[pair2.index(i)]:
                    temp.pop()
                else:
                    return False
        if len(temp) != 0:
            return False
        else:
            return True

code20 = Solution()
# print(code20.isValid("()"))
# print(code20.isValid("()[]{}"))
# print(code20.isValid("(]"))
# print(code20.isValid("([)]"))
# print(code20.isValid("{[]}"))
# print(code20.isValid("{{"))
print(code20.isValid(")("))