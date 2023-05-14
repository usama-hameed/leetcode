from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        limit = len(nums)
        for i in range(0, limit+1):
            if i not in nums:
                return i


s = Solution()
print(s.missingNumber([3, 0, 1]))
