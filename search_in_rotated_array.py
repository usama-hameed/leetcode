from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] < nums[mid] or target < nums[start]:
                    end = mid + 1
                else:
                    start = mid - 1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
