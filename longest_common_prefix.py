from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        final = []
        for i in zip(*strs):
            i = set(i)
            if len(i) == 1:
                final.append(list(i)[0])
            else:
                return ''.join(final)
        if not final:
            return ""
        else:
            return ''.join(final)


s = Solution()
print(s.longestCommonPrefix(["a"]))
