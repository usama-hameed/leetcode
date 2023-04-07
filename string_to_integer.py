class Solution:
    def myAtoi(self, s: str) -> int:

        if len(s) < 2 and not s.isdigit():
            return 0

        final_number = ''
        negative = False
        alpha = False
        index = 0
        while not alpha and index < len(s):
            if s[index] == '-':
                negative = True
            elif s[index].isdigit() or s[index] == " ":
                final_number = final_number + s[index]
            elif s[index] == '+' and not negative:
                alpha = True
            else:
                alpha = True
            index = index + 1

        if final_number:
            final_number = int(final_number.strip())
            if negative:
                final_number = int(final_number) * (-1)
            final_number = self.check_limit(final_number)
            return final_number

        else:
            return 0

    def check_limit(self, num):
        if num > pow(2, 31)-1 or num < pow(-2, 31):
            if num < 0:
                return pow(-2, 31)
            else:
                return pow(2, 31)
        else:
            return num

s = Solution()
print(s.myAtoi("+-42"))
