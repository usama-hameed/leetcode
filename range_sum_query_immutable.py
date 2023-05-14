from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


nums = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

obj = NumArray(nums[0][0])
final = []
nums.pop(0)
for n in nums:
    left, right = n[0], n[1]
    # param_1 = obj.sumRange(left,right)
    final.append(obj.sumRange(left, right))

print(final)
