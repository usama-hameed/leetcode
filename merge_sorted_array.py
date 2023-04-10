from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        new_index = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[new_index]
            new_index += 1
        nums1.sort()


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
