class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        first_ptr = 0
        second_ptr = len(s) - 1
        total = 0
        s = [i for i in s]
        while first_ptr < second_ptr:
            if s[first_ptr] < s[second_ptr]:
                s[second_ptr] = s[first_ptr]

            elif s[first_ptr] > s[second_ptr]:
                s[first_ptr] = s[second_ptr]
            if s[:] == s[::-1]:
                total += 1
                return ''.join(s)
            first_ptr += 1
            second_ptr -= 1
        return ''.join(s)

s = Solution()
print(s.makeSmallestPalindrome("egcfe"))
