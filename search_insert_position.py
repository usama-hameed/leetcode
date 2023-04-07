from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
        return start


s = Solution()
print(s.searchInsert([1,3,5,6], 5))
