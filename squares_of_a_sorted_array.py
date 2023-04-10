from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = list(map(lambda a: a**2, nums))
        nums.sort()
        return nums


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
