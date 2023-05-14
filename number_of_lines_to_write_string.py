from typing import List
import string


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alphabets = list(string.ascii_lowercase)
        pixel = 0
        line = 1
        for a in s:
            index = alphabets.index(a)
            if widths[index] + pixel <= 100:
                pixel = widths[index] + pixel
            else:
                line += 1
                pixel = 0
                pixel = pixel + widths[index]
        return [line, pixel]


s = Solution()
s.numberOfLines(widths=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                s="abcdefghijklmnopqrstuvwxyz")
