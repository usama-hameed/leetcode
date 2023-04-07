class Solution:
    def isPalindrome(self, s: str) -> bool:

        original = ''.join([i.lower() for i in s if i.isalnum()])
        if original[:] == original[::-1]:
            return True
        else:
            return False


s = Solution()
print(s.isPalindrome(' '))
