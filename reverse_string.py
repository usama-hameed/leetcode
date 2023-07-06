from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start_ptr = 0
        end_ptr = len(s) - 1

        while start_ptr < end_ptr:
            temp = s[start_ptr]
            s[start_ptr] = s[end_ptr]
            s[end_ptr] = temp
            start_ptr += 1
            end_ptr -= 1


s = Solution()
s.reverseString(["h","e","l","l","o"])
