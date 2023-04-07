class Solution:
    def reverse(self, x: int) -> int:

        x = str(x)
        if '-' not in x:
            n = int(x[::-1])
        else:
            x = x[1:]
            n = int(x[::-1]) * (-1)
        if n > pow(2, 31)-1 or n < pow(-2, 31):
            return 0
        else:
            return n


s = Solution()
print(s.reverse(-123))
