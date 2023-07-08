from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        first_ptr = 0
        second_ptr = 1
        third_ptr = 2
        final = set()
        while third_ptr < len(nums):
            if nums[second_ptr] - nums[first_ptr] == diff and nums[third_ptr] - nums[second_ptr] == diff:
                final.add((first_ptr, second_ptr, third_ptr))

            if third_ptr == len(nums) - 1:

                second_ptr += 1
                third_ptr = second_ptr

            if second_ptr == len(nums) - 1:
                first_ptr += 1
                second_ptr = first_ptr + 1
                third_ptr = second_ptr

            third_ptr += 1

        return len(final)


s = Solution()
print(s.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
