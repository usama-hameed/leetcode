class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False

        seen = []

        while n != 1 and n not in seen:
            seen.append(n)

            n = sum(int(i)**2 for i in str(n))

        return True if n == 1 else False


s = Solution()
print(s.isHappy(2))
