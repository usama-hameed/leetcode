# class Solution:
#     def reverseWords(self, s: str) -> str:
#         new_s = s.split(" ")
#         for index, value in enumerate(new_s):
#             new_s[index] = value[::-1]
#
#         return ' '.join(new_s)
#


#################### Second Solution ###########################3

class Solution:
    def reverseWords(self, s: str) -> str:
        inner_str = ''
        final_str = ''

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                final_str = " "+ inner_str + final_str
                inner_str = ''
            else:
                inner_str += s[i]
        return inner_str + final_str


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
