from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []

        for nums in nums1:
            if nums in nums2 and nums not in final:
                final.append(nums)

        return final


s = Solution()
s.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
