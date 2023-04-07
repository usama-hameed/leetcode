class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        sub_str = ''
        all_sub_strs = []
        for i in s:
            if i not in sub_str:
                sub_str += i
            else:
                sub_str = sub_str[sub_str.find(i):] + i
        print(sub_str)
        # if sorted_all_sub_strs:
        #     return sorted_all_sub_strs[0][1]


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))
