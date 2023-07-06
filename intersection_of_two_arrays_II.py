from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        final = []

        for i in nums1:
            if i in nums2:
                final.append(i)
        return final


s = Solution()
print(s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))