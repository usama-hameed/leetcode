from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        final = []
        upper, lower = 0, len(nums) - 1



s = Solution()
print(s.searchRange(nums = [1,2,2], target = 2))
