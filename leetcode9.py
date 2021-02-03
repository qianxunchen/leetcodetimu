class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x < 0:
            return False
        if 0 <= x < 10:
            return True
        else:
            str_x = str(x)
            lenght = len(str_x)
            if str_x[0] != str_x[-1]:
                return False
            while lenght:
                if str_x[lenght-1] == str_x[-lenght]:
                    lenght = lenght - 1
                else:
                    return False
            return True


code9 = Solution()
print(code9.isPalindrome(123))

