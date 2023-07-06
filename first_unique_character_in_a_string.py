class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, value in enumerate(s):
            if value not in s[:index] and value not in s[index+1:]:
                return index

s = Solution()
print(s.firstUniqChar("uussam"))
