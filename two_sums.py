from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collect = {}

        for index, num in enumerate(nums):
            if num in collect:
                return [index, collect[num]]
            diff = target - num
            if diff not in collect:
                collect[diff] = index


s = Solution()
print(s.twoSum([2,7,11,15], 9))
