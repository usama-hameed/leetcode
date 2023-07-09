class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        for index, value in enumerate(word):
            if value == ch:
                return word[0:index+1][::-1] + word[index+1:]
        return word


s = Solution()
print(s.reversePrefix("abcd", "z"))
