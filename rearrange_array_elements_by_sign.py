from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg_arr, pos_arr = [i for i in nums if i < 0], [i for i in nums if i > 0]
        final = []
        for first, second in zip(pos_arr, neg_arr):
            final.append(first)
            final.append(second)
        return final


"""
[0,1,2,-3,-4,-5,4,5,-6, -7]
[0,-3,1,-4,4,-5,5,-6,-7, 8]
"""

s = Solution()
print(s.rearrangeArray([3, 1, -2, -5, 2, -4]))
