class Solution:
    def lengthOfLongestSubstring(self, s):
        max_str = []
        max_lenght = []
        if len(s) == 0:
            return 0
        for i in s:
            if i not in max_str:
                max_str.append(i)
            else:
                max_lenght.append(len(max_str))
                max_str = max_str[max_str.index(i)+1:]
                max_str.append(i)
        max_lenght.append(len(max_str))
        if len(max_lenght) == 0:
            max_lenght.append(len(s))
        max_lenght.sort(reverse=True)
        return max_lenght[0]


code3 = Solution()
print(code3.lengthOfLongestSubstring("pwwekw"))