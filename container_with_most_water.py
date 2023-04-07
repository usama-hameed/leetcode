from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        res = 0
        while start < end:
            area = (end - start) * min(height[start], height[end])
            res = max(res, area)

            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return res


s = Solution()
print(s.maxArea([1, 1]))
