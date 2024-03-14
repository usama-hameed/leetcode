from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []
        for n1 in nums1:
            if n1 in nums2:
                break_num2 = False
                index = nums2.index(n1)
                for n2 in nums2[index:]:
                    if n2 > n1:
                        final.append(n2)
                        break_num2 = True
                        break
                if not break_num2:
                    final.append(-1)
        return final


s = Solution()
print(s.nextGreaterElement([2, 4], [1, 2, 3, 4]))
