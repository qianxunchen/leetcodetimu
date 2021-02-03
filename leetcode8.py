class Solution:
    def myAtoi(self, s):
        if len(s) == 0:
            return 0
        a = ""
        b = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "+"]
        bb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        s = s.lstrip()
        if s[0] not in b:
            return 0
        elif s[0]=="-":
            for i in range(1,len(s)):
                if s[i] not in bb:
                    break
                else:
                    a = a + s[i]
            a = "-" + a
        elif s[0] == "+":
            for i in range(1,len(s)):
                if s[i] not in bb:
                    break
                else:
                    a = a + s[i]
            a = "+" + a
        else:
            for i in range(len(s)):
                if s[i] not in bb:
                    break
                else:
                    a = a + s[i]
        if a != "" and a not in ["-","+"]:
            a = int(a)
            if a > 2 ** 31 - 1:
                a = 2 ** 31 - 1
            if a < -2 ** 31:
                a = -2 ** 31
            return a
        else:
            return 0

code8 = Solution()
print(code8.myAtoi(""))
# print(code8.myAtoi("21"))