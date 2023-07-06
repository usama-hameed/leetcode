from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first_ptr = 0
        second_ptr = 1
        sum = 0
        while sum != target or first_ptr < len(nums) - 1:
            sum = nums[first_ptr] + nums[second_ptr]
            if sum == target:
                return [first_ptr, second_ptr]
            if second_ptr == len(nums) - 1:
                first_ptr += 1
                second_ptr = first_ptr + 1
            else:
                second_ptr += 1


s = Solution()
print(s.twoSum([3,2,4], 6))
