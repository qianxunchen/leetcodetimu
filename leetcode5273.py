'''
移除石子最大的分数
'''
class Solution:
    def maximumScore(self, a, b, c):
        if a == 1 and b == 1 and c == 1:
            return 1
        res = 0
        nums = []
        nums.append(a)
        nums.append(b)
        nums.append(c)
        nums = sorted(nums)
        None_num = 0
        while None_num < 2:
            nums = sorted(nums)
            num_max = nums[-1]
            nums.pop(-1)
            num_min = nums[0]
            nums.pop(0)

            num_max -= 1
            num_min -= 1
            res += 1

            if num_min == 0:
                None_num = None_num + 1
            else:
                nums.append(num_min)
            if num_max == 0:
                None_num = None_num +1
            else:
                nums.append(num_max)

        return res




code5273 = Solution()
print(code5273.maximumScore(1,8,8))
print(code5273.maximumScore(4,4,6))
print(code5273.maximumScore(2,4,6))


