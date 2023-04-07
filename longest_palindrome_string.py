class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        # sub_str = ''
        final = []
        s = [i for i in s]

        for i in range(len(s)):
            sub_str = ''
            sub_str += s[i]
            for j in range(i+1, len(s)):
                sub_str += s[j]
                if s[i] == s[j] and sub_str[:] == sub_str[::-1]:
                    final.append((sub_str, len(sub_str)))
        # print(final)
        final = sorted(final, key=lambda x: x[1], reverse=True)
        if final:
            return final[0][0]
        else:
            return s[0]


s = Solution()
print(s.longestPalindrome("aaaaaa"))
