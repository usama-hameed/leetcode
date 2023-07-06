from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first_ptr = 0
        second_ptr = 1
        third_ptr = 2
        final = []
        first = []
        while third_ptr < len(nums):
            if nums[first_ptr] + nums[second_ptr] + nums[third_ptr] == 0:
                if [nums[first_ptr], nums[second_ptr], nums[third_ptr]].sort() not in final:
                    final.append([nums[first_ptr], nums[second_ptr], nums[third_ptr]])
            if second_ptr == len(nums) - 1:
                first_ptr +=1
                second_ptr = first_ptr + 1
                third_ptr = second_ptr + 1
            else:
                second_ptr += 1
                third_ptr += 1
        return final




s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
