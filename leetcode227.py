'''
基本计算器
'''
class Solution:
    def calculate(self, s):
        import re
        data = re.split('[+*-/]', s)
        tt = re.findall('[+*-/]', s)
        temp = []
        for i in range(len(tt)):
            if data[i] != "" and data[i] != " ":
                temp.append(int(data[i]))
            if tt[i] != " " and tt[i] != "":
                temp.append(tt[i])

        temp.append(data[-1])
        if len(temp) == 1:
            return int(temp[0])

        res = []
        n = 0
        while n < len(temp):
            if str(temp[n]) not in "*/":
                res.append(temp[n])
            elif temp[n] == "*":
                t = int(res[-1]) * int(temp[n + 1])
                res.pop()
                res.append(t)
                n+=1
            elif temp[n] == "/":
                t = int(int(res[-1]) / int(temp[n + 1]))
                res.pop()
                res.append(t)
                n+=1
            n += 1

        temp = res
        # print(temp)
        res = temp[0]
        n = 1
        if len(temp) == 1:
            return temp[0]
        while n < len(temp) - 1:
            if temp[n] == "+":
                res = int(res) + int(temp[n + 1])
            elif temp[n] == "-":
                res = int(res) - int(temp[n + 1])
            n += 1
        return res


code = Solution()
print(code.calculate(" 3+5 / 2 "))
print(code.calculate("0"))
print(code.calculate("  11"))
print(code.calculate("5  "))
print(code.calculate("3/2+1+1"))
print(code.calculate("1+1"))
print(code.calculate("1+1+1"))
print(code.calculate("3+2*2"))
print(code.calculate("2*3*4"))

